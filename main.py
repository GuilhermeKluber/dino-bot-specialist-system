from modules.dino_manager import DinoManager
import pyautogui
import time

def main():
    dino_manager = DinoManager()

    dino_manager.initialize_dino()
    while 1:
        obstacle = dino_manager.get_game_info()
        if obstacle.distance < 30 and obstacle.in_game:
            pyautogui.press("space")
            time.sleep(0.200)
        print(obstacle)

if __name__ == '__main__':
    main()