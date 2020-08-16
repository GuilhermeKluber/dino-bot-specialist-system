from durable.lang import *
import pyautogui

'''
Variáveis Length, Heigth, Speed, Distance, object
'''


with ruleset('Action'):


    @when_all((m.length < 20) & (m.height < 30) & (m.speed< 0.40 ) & (m.distance < 160))
    def jump_smaller(c):
        pyautogui.press("space")
        time.sleep(0.135)

    @when_all((m.length < 40) & (m.height<30) & (m.speed< 0.40 ) & (m.distance < 150) )
    def jump(c):
        pyautogui.press("space")
        time.sleep(0.135)

    @when_all((m.length > 40) & (m.height<30) & (m.speed< 0.40 ) & (m.distance < 130) )
    def jump1(c):
        pyautogui.press("space")
        time.sleep(0.135)
    
    @when_all((m.length < 40) &  (m.height>30) & (m.speed< 0.40 ) & (m.distance < 120))
    def jump2(c):
        pyautogui.press("space")
        time.sleep(0.135)

    @when_all((m.length > 40) &  (m.height>30) & (m.speed< 0.40 ) & (m.distance < 140))
    def jump3(c):
        pyautogui.press("space")
        time.sleep(0.135)



