import time
import pyautogui
# let the programm sleep before start
time.sleep(5)


j=0

# difine where to start drawing 
x=400
y=300
#deffin where is the color palet y cordinates
b=62
while j <2:
    #deffin where is the color palet X cordinates
    a=760
    
    
    i=0
    while i<10:
        pyautogui.moveTo(a,b)
        time.sleep(1)
        pyautogui.click()
        i=i+1
        a=a+22
# un comment next to draw extra shapes....
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
    # move the mouse to anothe place in the color palet..
    b=b+22
    j=j+1
    ## plaes be nise and sub to my youtube chanel...
