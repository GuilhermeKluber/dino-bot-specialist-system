import pyautogui
from durable.lang import *

'''
Variáveis Length, Heigth, Speed, Distance, object
'''
def press_space():
    pyautogui.keyUp('down')
    pyautogui.press("space", interval=0.135)
    
def press_down():
    pyautogui.keyDown('down')

with ruleset('Action'):

    @when_all((m.length < 20) & (m.height < 30) & (m.speed< 0.40 ) & (m.distance < 130) & (m.type=="land"))
    def jump_smaller(c):
        press_space()

    @when_all((m.length < 40) & (m.height<30) & (m.speed< 0.80 ) & (m.distance < 140) & (m.type=="land"))
    def jump(c):
        press_space()

    @when_all((m.length > 40) & (m.height<30) & (m.speed< 0.80 ) & (m.distance < 80) & (m.type=="land"))
    def jump1(c):
        press_space()
    
    @when_all((m.length < 40) &  (m.height>30) & (m.speed< 0.80 ) & (m.distance < 90) & (m.type=="land"))
    def jump2(c):
        press_space()

    @when_all((m.length > 40) &  (m.height>30) & (m.speed< 0.80 ) & (m.distance < 75) & (m.type=="land"))
    def jump3(c):
        press_space()

    @when_all((m.length < 60) & (m.distance < 150) & (m.type=="air"))
    def jump4(c):
        press_down()

        




