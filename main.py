from modules.dino_manager import DinoManager

def main():
    dino_manager = DinoManager()

    dino_manager.initialize_dino()
    while 1:
        dino_manager.get_game_info()

if __name__ == '__main__':
    main()