import pyautogui
import time


#x=352, y=222







#
# pyautogui.sleep(5)
# print(pyautogui.position())











# ScreenShot


# pyautogui.screenshot()



# Short project work

# x=397, y=1074
# x=1490, y=505
# x=1218, y=125
# x=1257, y=318

# songName = input("Enter your song name : ")
# pyautogui.sleep(2)
# # print(pyautogui.position())
# pyautogui.moveTo(397,1074,2,pyautogui.easeInQuad)
# pyautogui.click()
# pyautogui.moveTo(1490,505,2,pyautogui.easeInQuad)
# pyautogui.click()
# pyautogui.moveTo(1218,125,2,pyautogui.easeInQuad)
# pyautogui.click()
# pyautogui.write(songName, interval=0.1)
# pyautogui.press('enter')
# pyautogui.moveTo(1257,318,2,pyautogui.easeInQuad)
# pyautogui.click()



# Massage Box
#Big problem
# pyautogui.alert(text='Alert', title='alert', button='ok')
#pyautogui.confirm(text='Alert', title='alert box', button=['ok','cencel'])
# pyautogui.prompt(text='input', time='alert', default='username')
# pyautogui.password(text='Alert', time='alert', default='username')


#Keyboard Function

# for sample project
# pyautogui.click( x=1117, y=758)





# pyautogui.sleep(3)
# pyautogui.hotkey('ctrl','a')
# pyautogui.press('delete')


# pyautogui.sleep(3)
# i=0
# while i<=10:
#     pyautogui.keyDown('shift')
#     pyautogui.press('left')
#     pyautogui.keyUp('shift')
#     i=i+1

#
# pyautogui.sleep(3)
# pyautogui.write("https://www.youtube.com/watch?v=h18XqpKH7tI", interval=0.1)
# pyautogui.press("enter")



# Mouse Scroll
# pyautogui.sleep(2)
# pyautogui.scroll(-100000)


#Mouse up and Down

# pyautogui.sleep(2)
# pyautogui.mouseDown()
# pyautogui.mouseUp()



# Mouse click

# time.sleep(3)
# pyautogui.tripleClick()
# pyautogui.doubleClick(x=,y=)
# pyautogui.click()
# pyautogui.rightClick()
# pyautogui.leftClick()




# Drag Drag to

# pyautogui.drag(100,100)
# pyautogui.dragTo(120,120)




#Ease

# pyautogui.moveTo(100,100,2,pyautogui.easeInQuad) #start slow, end fast
#pyautogui.moveTo(300,200,2, pyautogui.easeOutQuad) #start fast , end slow
#pyautogui.moveTo(300,200,2, pyautogui.easeInOutQuad) #start fast , end slow
#pyautogui.moveTo(300,200,2, pyautogui.easeInBounce) #start fast , end slow#move to
#pyautogui.moveTo(300,200,2, pyautogui.easeInOutElastic) #start fast , end slow#move to
# pyautogui.moveTo(100,0)


# Move
# pyautogui.move(500,0)

#Practice problem

# while True:
#     posi = pyautogui.position()
#     print(posi)
#     time.sleep(2)




#MOuse movement
# try:
#     pyautogui.FAILSAFE = False
#     pyautogui.PAUSE = 5
#     pyautogui.moveTo(0, 0)
#     pyautogui.PAUSE = 5
#     pyautogui.moveTo(10, 20)
# except pyautogui.FailSafeException:
#     print("Error")




# onsc=pyautogui.onScreen(200,200)
# size=pyautogui.size()
# posi=pyautogui.position()
# print(posi)
# print(onsc)
# print(size)


