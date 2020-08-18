from modules.dino_manager import DinoManager
from modules.knowledge_base import *
from durable.lang import *
import pyautogui
import time
import pandas as pd

def main():
    dino_manager = DinoManager()
    dino_manager.initialize_dino()

    time_start = time.time()
    offset = 0
    while 1:
        obstacle = dino_manager.get_game_info()

        if obstacle.in_game:

            time_elapsed = time.time() - time_start
            if time_elapsed>20 and time_elapsed<22:
                offset = 10
            elif time_elapsed>30 and time_elapsed<32:
                offset = 20

            elif time_elapsed>50 and time_elapsed<55:
                offset = 30

            data = {
                    "length":obstacle.length, 
                    "height":obstacle.height,
                    "speed":obstacle.speed, 
                    "distance": obstacle.distance-offset,
                    "object":obstacle.in_game,
                    "type": obstacle.type,
                    "timeElapsed": time_elapsed
                    }
            try:
                post('Action', data)
            except Exception as e:
                pass
            # list_data.append(data)
        
            # print(data)
        # if time.time()-time_start>120:
        #     break
    # df_data = pd.DataFrame(list_data)
    # df_data.to_csv(f'./files/{str(int(time.time()))}_data.csv',index=False)

if __name__ == '__main__':
    main()