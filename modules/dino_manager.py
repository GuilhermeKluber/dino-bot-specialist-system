import os
import cv2
import time
import pyautogui
import webbrowser
import numpy as np
import collections
from mss import mss
from datetime import datetime
from modules.utils import binarize_image, cronometra
from modules.obstacle import Obstacle

class DinoManager():
    def __init__(self):
        self.last_obstacle = Obstacle(1,1,[999,0,999,999])
        self.last_obstacle.in_game = False
        self.last_speed = 1
        self.history_dino_color = collections.deque(maxlen=15)
        self.dino_color = 83
        self.game_over = collections.deque(maxlen=25)
        # self.t_rex_head = 420, 308, 454, 372
        # self.game_x, self.game_y, self.game_x2, self.game_y2 = 450, 275, 972, 376
        # self.last_game_image = self.grab_image(self.game_x, self.game_y, self.game_x2, self.game_y2)[:,:,0]

    def show_without_stop(self,window,image):
        """
        Show a image.
        :param image: A image in array format 

        """
        cv2.imshow(window,image)
        if cv2.waitKey(2) ==  27:
            cv2.destroyAllWindows()

    def open_dino_website(self):
        url = "https://chromedino.com/"
        webbrowser.open(url)
        time.sleep(5)

    def initialize_dino(self):
        self.open_dino_website()
        time.sleep(2)
        try:
            x, y, w, h = pyautogui.locateOnScreen("./images/t_rex.png")
            # x, y, w, h = 377,343,47,50 # SET by GREG
            game_x = x + w
            game_y2 = y + h
            print("LOG [INFO] Position of 'T Rex' image ", x, y, w, h)
            pyautogui.press("space")
            time.sleep(2)
            tx, ty, tw, th = pyautogui.locateOnScreen("./images/t_rex_head.png")
            # tx, ty, tw, th = 377,343,47,50 # SET by GREG
            print("LOG [INFO] Position of 'T Rex Head' image ", x, y, w, h)

            time.sleep(8)
            x, y, w, h = pyautogui.locateOnScreen("./images/hi.png")
            # x, y, w, h = 804,257,32,22 # SET by GREG
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
        self.game_x, self.game_y, self.game_x2, self.game_y2 = game_x + int(fix_x), game_y, game_x2 + int(fix_x2), game_y2 - 13 
        # o -13 é para remover o chão na hora de encontrar os objetos 
        self.last_game_image = self.grab_image(self.game_x, self.game_y, self.game_x2, self.game_y2)[:,:,0]

        print("LOG [INFO] Position of 'T Rex Head' image ", tx , ty-th, tx + tw, ty + th)
        print("LOG [INFO] Game Position ", self.game_x, self.game_y, self.game_x2, self.game_y2)

    def grab_image(self, x,y,x2,y2):
        monitor = {'left': x, 'top': y, 'width': x2 - x, 'height': y2 - y}
        with mss() as sct:
            image = sct.grab(monitor);
        img = np.array(image);
        return img
        
    # @cronometra
    def get_game_info(self):
        obstacle = self.get_obstacle_info()

        if obstacle and obstacle.distance > 0:
            obstacle.calculate_speed(self.last_obstacle)
            self.last_speed = obstacle.speed
            self.last_obstacle = obstacle
        else:
            self.last_obstacle.in_game = False
        return self.last_obstacle

    def get_dino_color(self,image):
        # Conta os pixeis mais frequentes para achar o valor da cor do dino
        
        res = collections.Counter(image.flat).most_common()
        if len(res) > 1:
            self.history_dino_color.append(res[1][0])
        else :
            self.history_dino_color.append(res[0][0])
        self.dino_color = collections.Counter(self.history_dino_color).most_common()[0][0]

    def join_objects(self, objects, threshold):
        accepted_rects = []

        objects.sort(key = lambda x : x[0])
        objects_used = [False for i in range(len(objects))]
        for idx, bbox in enumerate(objects):
            if (objects_used[idx] == False):

                x, x2, y, y2 = bbox[0], bbox[0] + bbox[2], bbox[1], bbox[1] + bbox[3]
                objects[idx] = True
                for sub_idx, sub_bbox in enumerate(objects[(idx+1):], start = (idx+1)):
                    xx, xx2, yy, yy2 = sub_bbox[0], sub_bbox[0] + sub_bbox[2], sub_bbox[1], sub_bbox[1] + sub_bbox[3]

                    if (xx <= x2 + threshold):
                        x2, y, y2 = xx2, min(y, yy), max(y2, yy2)
                        objects_used[sub_idx] = True
                    else:
                        break
                accepted_rects.append([x, y, x2, y2 ])
        return accepted_rects

    def check_if_game_is_over(self, actual_image, last_image):
        res = np.sum((actual_image - last_image))
        status_game = False
        if res == 0:
            status_game=True
        self.game_over.append(status_game)

    # @cronometra
    def get_obstacle_info(self):
        # TODO: Separe get obstacle information from game over check
        s = 0
        length = 0
        height=0

        game_image = self.grab_image(self.game_x, self.game_y, self.game_x2, self.game_y2) 
        t_rex_image = self.grab_image(*self.t_rex_head) 

        dino_color = self.get_dino_color(t_rex_image[:,:,0])
        size = game_image.shape
        
        binarized_image = binarize_image(game_image,self.dino_color)

        self.check_if_game_is_over(self.last_game_image, binarized_image)

        self.last_game_image = binarized_image.copy()

        obstacles = []
        _, contours, _= cv2.findContours(binarized_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            for c in contours:
                x,y,w,h = cv2.boundingRect(c)
                if w > 3 and h >3:
                    
                    obstacles.append([x,y,w,h])


        to_show = cv2.cvtColor(binarized_image,cv2.COLOR_GRAY2BGR)
        obstacles = self.join_objects(obstacles, 10)
        for x,y,x2,y2 in obstacles:
            cv2.rectangle(to_show, (x,y), (x2,y2), (0,255,0),1)

        # self.show_without_stop("T-Rex",t_rex_image[:,:,0])
        # self.show_without_stop("Game",to_show)

        if len(obstacles) > 0:
            next_obstacle = Obstacle(self.last_speed, self.game_y2 - self.game_y, obstacles[0])
            return next_obstacle
        else:
            return None


