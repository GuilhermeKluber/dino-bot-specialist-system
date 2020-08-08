from datetime import datetime
import numpy as np
import webbrowser
import pyautogui
import time
import cv2
import os


class DinoManager():
    def __init__(self):
        self.initialize_dino()
        self.last_obstacle = {}
        self.last_speed = 0
        self.lx,self.ly,self.rx,self.ry = lx,ly,rx,ry

    def obstacle(self,distance, length, speed, time,height,moviment = None):
        return { 'distance': distance, 'length': length, 'speed': speed, 'time': time,'height':height,"moviment": moviment }

    def open_dino_website(self):
        url = "https://chromedino.com/"
        webbrowser.open(url)
        time.sleep(3)

    def initialize_dino(self):
        #TODO: Validate that its working
        self.open_dino_website()
        try:
            lx, ly, w, h = pyautogui.locateOnScreen("./images/t_rex.png")
            ly += h
            pyautogui.press("space")
            time.sleep(2)
            t_rex, _, w, h = pyautogui.locateOnScreen("./images/t_rex_head.png")

            t_rex += w
            time.sleep(8)
            rx, ry, w, h = pyautogui.locateOnScreen("./images/hi.png")
        except:
            print("Game Not Found")
            raise Exception("Game not found!")

        ly, ry = ry, ly
        self.left, self.top, self.right, self.bottom = lx, ly, rx, ry

    def get_game_info(self,game_over):
        #TODO: Validate that its working
        #TODO: Get speed, obstacle information and check game status
        dist,game_over,length,height = self.get_obstacle_info(game_over)
        time = datetime.now()
        delta_dist = 0
        speed = self.last_speed
        if self.last_obstacle:
            delta_dist = self.last_obstacle['distance'] - dist
            speed = (delta_dist / ((time - self.last_obstacle['time']).microseconds)) * 10000
            if not (speed/10 > 0.1 and speed/10 < 1):
                speed = self.last_speed
            else:
                self.last_speed = speed
        self.last_obstacle = obstacle(dist, length, speed, time,height)
        return self.last_obstacle, game_over

    def get_dino_color(self,image):
        size = image.size
        dino_color = image.getpixel((size[0]-40,15))
        th = np.array(image)
        to_compare = image.getpixel((1,1))
        count=0
        for i in range(size[1]):
            if not th[-i][50][0] == to_compare[0]:
                count+=1
                if count == 4:
                    dino_color = th[-i][50]
                    return dino_color
        return dino_color

    def check_game_status(self):
        # TODO: Verify if game is over

    def get_obstacle_info(self,game_over):
        # TODO: Separe get obstacle information from game over check

        s = 0
        length = 0
        height=0
        image = pyautogui.screenshot(region=(self.lx,self.ly, self.rx-self.lx+160, self.ry-self.ly-10))
        DinoColor = self.get_dino_color(image)
        size = image.size
        image = np.array(image)
        th = compare(image,DinoColor)
        x_aux=1000000
        count=1
        _, contours, _= cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 1:
            for c in contours:
                x,y,w,h = cv2.boundingRect(c)
                if cv2.contourArea(c)>850 and cv2.contourArea(c)<1000:
                    if (x > size[0]/2-50) and (y < size[1]-10):
                        game_over=True
                        print("Game Over!!!")
                        return 286,game_over,0, 0
                if cv2.contourArea(c)>120 and cv2.contourArea(c)<450:
                    if abs(x_aux-x) < 30 :
                        count+=1
                    if x < x_aux and x >70:
                        length=w
                        x_aux=x
                        if not y+h >= size[1]-15:
                            height=size[1]-(h+y)
            if x_aux > 70 and x_aux < size[0]:
                return (x_aux-70), game_over, length*count, height

        return 286,game_over,0, 0

    def reset(self):
        self.last_obstacle = {}
        self.last_speed = 0