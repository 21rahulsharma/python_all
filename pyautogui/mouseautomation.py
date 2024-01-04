import pyautogui
import time
print("Screen Configuration: ",pyautogui.size())
time.sleep(2)
print("Current Mouse Position: ",pyautogui.position())

#Move The Mouse Pointer 
time.sleep(2)
pyautogui.moveTo(960,540) 
#To move the cursor relative to the current position
pyautogui.moveRel(50,70,1) #Third parameter is interval/duration
time.sleep(2)
#To drag te mouse pointer(hold click and move)
pyautogui.dragTo(500,400,button='left')
pyautogui.dragRel(550,490)

#to click
pyautogui.moveTo(54,8)
pyautogui.click()
# Double Click
#pyautogui.doubleClick()

