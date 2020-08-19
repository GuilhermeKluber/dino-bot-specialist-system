import pyautogui

class KeyboardAction:

    def __init__(self):
        pass

    def press_space_super_ultra_very_fast(self):
        pyautogui.keyUp('down')
        pyautogui.press("space", interval=0.05)
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')    

    def press_space_ultra_very_fast(self):
        pyautogui.keyUp('down')
        pyautogui.press("space", interval=0.075)
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
        
    def press_space_ultra_fast(self):
        pyautogui.keyUp('down')
        pyautogui.press("space", interval=0.1)
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')

    def press_space_fast(self):
        pyautogui.keyUp('down')
        pyautogui.press("space", interval=0.12)
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')

    def press_space(self):
        pyautogui.keyUp('down')
        pyautogui.press("space", interval=0.14)
        
    def press_down(self):
        pyautogui.keyDown('down')
