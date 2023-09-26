import time
import pyautogui
time.sleep(5)

j=0
x=400
y=300
b=62
while j <2:
    a=760
    i=0
    while i<10:
        pyautogui.moveTo(a,b)
        time.sleep(1)
        pyautogui.click()
        i=i+1
        a=a+22
        '''pyautogui.moveTo(x, y, duration = 1)
        pyautogui.dragRel(100, 0, duration = 1)
        pyautogui.dragRel(0, 100, duration = 1)
        pyautogui.dragRel(-100, 0, duration = 1)
        pyautogui.dragRel(0, -100, duration = 1)'''
    
        pyautogui.dragRel(50, 50, duration = 0.5)
        pyautogui.dragRel(-50, 50, duration = 0.5)
        pyautogui.dragRel(-50, -50, duration = 0.5)
        pyautogui.dragRel(50, -50, duration = 0.5)
        x=x+10
        y=y+10
    
    b=b+22
    j=j+1