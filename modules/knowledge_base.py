import inspect
import pyautogui
from durable.lang import ruleset, when_all, m

# TODO: map more rules, HI of dino 1002
# TODO: sometimes the rule is applied twice

def press_space_ultra_fast():
    pyautogui.keyUp('down')
    pyautogui.press("space", interval=0.11)
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

def press_space_fast():
    pyautogui.keyUp('down')
    pyautogui.press("space", interval=0.12)
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

def press_space():
    pyautogui.keyUp('down')
    pyautogui.press("space", interval=0.14)
    
def press_down():
    pyautogui.keyDown('down')

with ruleset('Action'):
    # 1 small cactus time < 30s
    @when_all((m.length>=15)&(m.length<=23)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=90)&(m.distance<=105)&
              (m.timeElapsed>=0)&(m.timeElapsed<=30)&
              (m.type=="land"))
    def jump_one_small_cactus1(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space_ultra_fast()

    # 1 small cactus time between 30s 40s
    @when_all((m.length>=15)&(m.length<=23)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=140)&(m.distance<=160)&
              (m.timeElapsed>=30)&(m.timeElapsed<=40)&
              (m.type=="land"))
    def jump_one_small_cactus2(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space_fast()

    # 1 small cactus time between 40s 120s
    @when_all((m.length>=15)&(m.length<=23)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=160)&(m.distance<=180)&
              (m.timeElapsed>=40)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_one_small_cactus3(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space()
        
    # 2 small cactus time 0s 50s
    @when_all((m.length>=27)&(m.length<=35)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=100)&(m.distance<=120)&
              (m.timeElapsed>=0)&(m.timeElapsed<=50)&
              (m.type=="land"))
    def jump_two_small_cactus1(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space()

    # 3 small cactus time 0s 50s
    @when_all((m.length>=45)&(m.length<=53)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=90)&(m.distance<=120)&
              (m.timeElapsed>=0)&(m.timeElapsed<=50)&
              (m.type=="land"))
    def jump_tree_small_cactus1(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space()

    # 1 big cactus 0s 30s
    @when_all((m.length>=20)&(m.length<=25)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=75)&(m.distance<=90)&
              (m.timeElapsed>=0)&(m.timeElapsed<=30)&
              (m.type=="land"))
    def jump_one_big_cactus1(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space_fast()

    # 1 big cactus 30s 120s
    @when_all((m.length>=20)&(m.length<=25)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=130)&(m.distance<=150)&
              (m.timeElapsed>=30)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_one_big_cactus2(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space()

    # 3 big cactus 0s 50s
    @when_all((m.length>=68)&(m.length<=75)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=80)&(m.distance<=120)&
              (m.timeElapsed>=0)&(m.timeElapsed<=50)&
              (m.type=="land"))
    def jump_tree_big_cactus1(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space()

    # 3 big cactus 5s 120s
    @when_all((m.length>=68)&(m.length<=75)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=80)&(m.distance<=110)&
              (m.timeElapsed>50)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_tree_big_cactus2(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space()
    
    # bird in air
    @when_all((m.distance<90)&
              (m.type=="air"))
    def down_bird(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_down()

    # bird in air
    @when_all((m.length>=40)&(m.length<=44)&
              (m.height>=20)&(m.height<=26)&
              (m.distance>=100)&(m.distance<=120)&
              (m.timeElapsed>=30)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_bird(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space()

    # General Rule
    @when_all((m.distance<100)&
              (m.type=="land"))
    def jump_general(c):
        print('LOG[DEBUG]',inspect.stack()[0][3])
        press_space()