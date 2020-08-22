import inspect
import pyautogui
from durable.lang import ruleset, when_all, m
from modules.keyboard_action import KeyboardAction

key_board = KeyboardAction()

def custom_print(function_desc, conds):
    print('LOG[DEBUG]',function_desc, conds.m.distance, conds.m.timeElapsed)

with ruleset('Action'):
    # 1 small cactus time < 15s
    @when_all((m.length>=15)&(m.length<=23)&
              (m.height>=19)&(m.height<=26)& 
              (m.distance>=0)&(m.distance<=80)&
              (m.timeElapsed>=0)&(m.timeElapsed<=15)&
              (m.type=="land"))
    def jump_one_small_cactus1(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_ultra_very_fast()

    # 1 small cactus time between 15s  30s
    @when_all((m.length>=15)&(m.length<=23)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=95)&
              (m.timeElapsed>=15)&(m.timeElapsed<=30)&
              (m.type=="land"))
    def jump_one_small_cactus2(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_ultra_very_fast()

    # 1 small cactus time between 30s 40s
    @when_all((m.length>=15)&(m.length<=23)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=150)&
              (m.timeElapsed>=30)&(m.timeElapsed<=40)&
              (m.type=="land"))
    def jump_one_small_cactus3(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_ultra_fast()

    # 1 small cactus time between 40s 60s
    @when_all((m.length>=15)&(m.length<=23)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=170)&
              (m.timeElapsed>=40)&(m.timeElapsed<=60)&
              (m.type=="land"))
    def jump_one_small_cactus4(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_ultra_fast()

    # 1 small cactus time between 60s 90s
    @when_all((m.length>=15)&(m.length<=23)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=210)&
              (m.timeElapsed>=60)&(m.timeElapsed<=90)&
              (m.type=="land"))
    def jump_one_small_cactus5(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_ultra_very_fast()

    # 1 small cactus time between 40s 90s
    @when_all((m.length>=15)&(m.length<=23)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=240)&
              (m.timeElapsed>=90)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_one_small_cactus6(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_super_ultra_very_fast()
        
    # 2 small cactus time < 30s
    @when_all((m.length>=27)&(m.length<=35)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=120)&
              (m.timeElapsed>=0)&(m.timeElapsed<=30)&
              (m.type=="land"))
    def jump_two_small_cactus1(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space()

    # 2 small cactus time 30s 50s
    @when_all((m.length>=27)&(m.length<=35)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=110)&
              (m.timeElapsed>=30)&(m.timeElapsed<=50)&
              (m.type=="land"))
    def jump_two_small_cactus2(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space()

    # 2 small cactus time 50s 80s
    @when_all((m.length>=27)&(m.length<=35)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=125)&
              (m.timeElapsed>=50)&(m.timeElapsed<=80)&
              (m.type=="land"))
    def jump_two_small_cactus3(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()

    # 2 small cactus time 80s 120s
    @when_all((m.length>=27)&(m.length<=35)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=130)&
              (m.timeElapsed>=80)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_two_small_cactus4(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()

    # 3 small cactus time 0s 50s
    @when_all((m.length>=45)&(m.length<=53)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=100)&
              (m.timeElapsed>=0)&(m.timeElapsed<=50)&
              (m.type=="land"))
    def jump_tree_small_cactus1(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space()

    # 3 small cactus time 50s 80s
    @when_all((m.length>=45)&(m.length<=53)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=130)&
              (m.timeElapsed>50)&(m.timeElapsed<=80)&
              (m.type=="land"))
    def jump_tree_small_cactus2(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()

    # 3 small cactus time 80s 120s
    @when_all((m.length>=45)&(m.length<=53)&
              (m.height>=19)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=160)&
              (m.timeElapsed>80)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_tree_small_cactus3(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()
 
    # 1 big cactus 0s 30s
    @when_all((m.length>=20)&(m.length<=25)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=85)&
              (m.timeElapsed>=0)&(m.timeElapsed<15)&
              (m.type=="land"))
    def jump_one_big_cactus0(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()

    # 1 big cactus 0s 30s
    @when_all((m.length>=20)&(m.length<=25)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=100)&
              (m.timeElapsed>=15)&(m.timeElapsed<=30)&
              (m.type=="land"))
    def jump_one_big_cactus1(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()

    # 1 big cactus 30s 120s
    @when_all((m.length>=20)&(m.length<=25)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=140)&
              (m.timeElapsed>=30)&(m.timeElapsed<=50)&
              (m.type=="land"))
    def jump_one_big_cactus2(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()

    # 1 big cactus 50s 120s
    @when_all((m.length>=20)&(m.length<=25)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=150)&
              (m.timeElapsed>=50)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_one_big_cactus3(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()

    # 2 big cactus < 30s
    @when_all((m.length>=45)&(m.length<=51)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=120)&
              (m.timeElapsed>=0)&(m.timeElapsed<=30)&
              (m.type=="land"))
    def jump_two_big_cactus1(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space()

    # 2 big cactus 30s 50s
    @when_all((m.length>=45)&(m.length<=51)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=130)&
              (m.timeElapsed>=30)&(m.timeElapsed<=50)&
              (m.type=="land"))
    def jump_two_big_cactus2(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space()

    # 2 big cactus 50s 120s
    @when_all((m.length>=45)&(m.length<=51)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=140)&
              (m.timeElapsed>=50)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_two_big_cactus3(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()

    # 3 big cactus 0s 50s
    @when_all((m.length>=68)&(m.length<=75)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=110)&
              (m.timeElapsed>=0)&(m.timeElapsed<=50)&
              (m.type=="land"))
    def jump_tree_big_cactus1(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space()

    # 3 big cactus 50s 80s
    @when_all((m.length>=68)&(m.length<=75)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=120)&
              (m.timeElapsed>50)&(m.timeElapsed<=80)&
              (m.type=="land"))
    def jump_tree_big_cactus2(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()

    # 3 big cactus 80s 120s
    @when_all((m.length>=68)&(m.length<=75)&
              (m.height>=35)&(m.height<=40)&
              (m.distance>=0)&(m.distance<=150)&
              (m.timeElapsed>80)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_tree_big_cactus3(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()
    
    # bird in air
    @when_all((m.distance>=0)&(m.distance<=100)&
              (m.type=="air"))
    def down_bird(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_down()

    # bird in air
    @when_all((m.length>=40)&(m.length<=44)&
              (m.height>=20)&(m.height<=26)&
              (m.distance>=0)&(m.distance<=120)&
              (m.timeElapsed>=30)&(m.timeElapsed<=120)&
              (m.type=="land"))
    def jump_bird(c):
        custom_print(inspect.stack()[0][3], c)
        key_board.press_space_fast()