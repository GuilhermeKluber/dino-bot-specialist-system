from datetime import datetime
from modules.utils import binarize_image, cronometra
from mss import mss
import numpy as np
import webbrowser
import collections
import pyautogui
import time
import cv2
import os


class DinoManager():
    def __init__(self):
        self.last_obstacle = None
        self.last_speed = 0
        self.display = True
        self.history_dino_color = collections.deque(maxlen=15)
        self.dino_color = 83

    def obstacle(self,distance, length, speed, time,height,moviment = None):
        return { 'distance': distance, 'length': length, 'speed': speed, 'time': time,'height':height,"moviment": moviment }

    def show(self,image):
        """
        Show a image.
        :param image: A image in array format 

        """
        if self.display : cv2.imshow("test",image)
        while 1:
            if cv2.waitKey(2) ==  27 or not self.display:
                break

    def show_without_stop(self,window,image):
        """
        Show a image.
        :param image: A image in array format 

        """
        if self.display : 
            cv2.imshow(window,image)
            if cv2.waitKey(2) ==  27:
                cv2.destroyAllWindows()

    def open_dino_website(self):
        url = "https://chromedino.com/"
        webbrowser.open(url)
        time.sleep(3)

    def initialize_dino(self):
        #TODO: Validate that its working
        self.open_dino_website()
        try:
            x, y, w, h = pyautogui.locateOnScreen("./images/t_rex.png")
            game_x = x + w
            game_y2 = y + h
            print("LOG [INFO] Position of 'T Rex' image ", x, y, w, h)
            pyautogui.press("space")
            time.sleep(2)
            tx, ty, tw, th = pyautogui.locateOnScreen("./images/t_rex_head.png")

            print("LOG [INFO] Position of 'T Rex Head' image ", x, y, w, h)

            time.sleep(8)
            x, y, w, h = pyautogui.locateOnScreen("./images/hi.png")
            print("LOG [INFO] Position of 'HI' (high score) image ", x, y, w, h)
            game_x2 = x
            game_y = y + h
    
        except: 
            print("Game Not Found")
            raise Exception("Game not found!")

        # Corrige distorção do jogo quando redimensiona janela do chrome
        fix_x = (game_y2 - game_y)/0.285 - (game_x2 - game_x)
        fix_x2 = (game_y2 - game_y)/0.21 - (game_x2 - game_x)

        self.t_rex_head = tx , ty-th, tx + tw, ty + th
        self.x, self.y, self.x2, self.y2 = game_x + int(fix_x), game_y, game_x2 + int(fix_x2), game_y2 - 13 
        # o -13 é para remover o chão na hora de encontrar os objetos 

        print("LOG [INFO] Game Position ", self.x, self.y, self.x2, self.y2)

    def grab_image(self, x,y,x2,y2):
        monitor = {'left': x, 'top': y, 'width': x2 - x, 'height': y2 - y}
        # The simplest use, save a screen shot of the 1st monitor
        with mss() as sct:
            image = sct.grab(monitor)
            
        img = np.array(image)
        return img

    def get_game_info(self):
        #TODO: Validate that its working
        #TODO: Get speed, obstacle information and check game status
        dist, length, height = self.get_obstacle_info()

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
        self.last_obstacle = self.obstacle(dist, length, speed, time,height)
        return self.last_obstacle

    def get_dino_color(self,image):
        # Conta os pixeis mais frequentes para achar o valor da cor do dino
        
        res = collections.Counter(image.flat).most_common()
        if len(res) > 1:
            self.history_dino_color.append(res[1][0])
        else :
            self.history_dino_color.append(res[0][0])
        self.dino_color = collections.Counter(self.history_dino_color).most_common()[0][0]

    def is_land_or_air(self):
        # TODO: Verify if object is land or air
        pass

    def join_objects(self, objects, threshold):
        accepted_rects = []

        objects.sort(key = lambda x : x[0])
        objects_used = [False for i in range(len(objects))]
        for idx, bbox in enumerate(objects):
            if (objects_used[idx] == False):

                # Initialize current rect
                x = bbox[0]
                x2 = bbox[0] + bbox[2]
                y = bbox[1]
                y2 = bbox[1] + bbox[3]

                # This bounding rect is used
                objects[idx] = True

                # Iterate all initial bounding rects
                # starting from the next
                for sub_idx, sub_bbox in enumerate(objects[(idx+1):], start = (idx+1)):

                    # Initialize merge candidate
                    xx = sub_bbox[0]
                    xx2 = sub_bbox[0] + sub_bbox[2]
                    yy = sub_bbox[1]
                    yy2 = sub_bbox[1] + sub_bbox[3]

                    # Check if x distance between current rect
                    # and merge candidate is small enough
                    if (xx <= x2 + threshold):

                        # Reset coordinates of current rect
                        x2 = xx2
                        y = min(y, yy)
                        y2 = max(y2, yy2)

                        # Merge candidate (bounding rect) is used
                        objects_used[sub_idx] = True
                    else:
                        break

                # No more merge candidates possible, accept current rect
                accepted_rects.append([x, y, x2 - x, y2 - y])
        return accepted_rects

    @cronometra
    def get_obstacle_info(self):
        # TODO: Separe get obstacle information from game over check

        s = 0
        length = 0
        height=0

        game_image = self.grab_image(self.x, self.y, self.x2, self.y2) 
        t_rex_image = self.grab_image(*self.t_rex_head) 

        dino_color = self.get_dino_color(t_rex_image[:,:,0])
        size = game_image.shape
        
        th = binarize_image(game_image,self.dino_color)
        x_aux=1000000
        count=1

        self.show_without_stop("head",t_rex_image[:,:,0])
        self.show_without_stop("game",th)
        # self.show_without_stop(th)
        objects = []
        _, contours, _= cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 1:
            for c in contours:
                x,y,w,h = cv2.boundingRect(c)
                if w > 3 and h >3:
                    objects.append([x,y,w,h])
        print(objects)
        objects = self.join_objects(objects, 10)
        print(objects)
        return (x_aux-70), length*count, height

        # return 286,0, 0

    def reset(self):
        self.last_obstacle = {}
        self.last_speed = 0