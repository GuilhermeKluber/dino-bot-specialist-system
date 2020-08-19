import time
import pyautogui
from durable.lang import post
from modules.knowledge_base import *
from modules.dino_manager import DinoManager

def main():
    
    dino_manager = DinoManager()
    dino_manager.initialize_dino()

    time_start = time.time()
    offset = 0

    # Auto
    pyautogui.press('SPACE',interval=0.135)
    time.sleep(2)
    # Manually
    # print('PRESS SPACE ON DINO GAME, you have 5 seconds to start process...')
    # time.sleep(5)
    
    while 1:
        obstacle = dino_manager.get_game_info()
        
        game_status = list(dino_manager.game_over)
        if len(game_status)==25 and all(game_status)==True:
            # raise Exception('GAME OVER')
            print('LOG[INFO] GAME OVER')
            dino_manager.game_over.clear()
            time.sleep(2)
            pyautogui.press('SPACE',interval=0.135)
            time_start = time.time()
            print('LOG[INFO] GAME RESTART')

        if obstacle.in_game: 

            time_elapsed = time.time() - time_start

            data = {
                    "length":obstacle.length, 
                    "height":obstacle.height,
                    "distance": obstacle.distance,
                    "timeElapsed": time_elapsed,
                    "type": obstacle.type
                    }
            print(data)
            try:
                post('Action', data)
            except Exception as e:
                pass

if __name__ == '__main__':
    main()