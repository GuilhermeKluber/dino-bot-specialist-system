from modules.dino_manager import DinoManager
from modules.knowledge_base import *
from durable.lang import *
import pyautogui
import time

def main():
    dino_manager = DinoManager()
    dino_manager.initialize_dino()

    while 1:
        obstacle = dino_manager.get_game_info()

        if obstacle.in_game:

            data = {
                    "length":obstacle.length, 
                    "height":obstacle.height,
                    "speed":obstacle.speed, 
                    "distance": obstacle.distance,
                    "object":obstacle.in_game
                    }
        try:
            post('Action', data)
            print(data)

        except Exception as e:
            pass

if __name__ == '__main__':
    main()