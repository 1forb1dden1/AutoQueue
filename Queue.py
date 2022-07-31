from pyautogui import *
import pyautogui
import time
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


#DON'T STEAL MY ACCOUNT ! ! !
username = "Picermor" 
password = "hysqlchix4"

#top, mid, bot, support, jungle, fill
role1 = "bot.JPG"
role2 = "mid.JPG"

#print("Enter Your Username: ")
#username = input()
#print("Enter Your Password: ")
#password = input()
print("Currently Logging in...")

if pyautogui.locateOnScreen('Username.JPG', confidence = 0.80):
    InputX = pyautogui.locateOnScreen('Username.JPG', confidence = 0.80).left+20
    InputY = pyautogui.locateOnScreen('Username.JPG', confidence = 0.80).top+30
    click(InputX, InputY)
    pyautogui.typewrite(username)
if pyautogui.locateOnScreen('Password.JPG', confidence = 0.80):
    InputX = pyautogui.locateOnScreen('Password.JPG', confidence = 0.80).left+20
    InputY = pyautogui.locateOnScreen('Password.JPG', confidence = 0.80).top+30
    click(InputX, InputY)
    pyautogui.typewrite(password)
if pyautogui.locateOnScreen('Login.JPG', confidence = 0.80):
    InputX = pyautogui.locateOnScreen('Login.JPG', confidence = 0.80).left+20
    InputY = pyautogui.locateOnScreen('Login.JPG', confidence = 0.80).top+30
    click(InputX, InputY)
while (pyautogui.locateOnScreen('ClientPlay.JPG', confidence = 0.95)) == None:
    if(pyautogui.locateOnScreen('Play.JPG', confidence = 0.80)):
        InputX = pyautogui.locateOnScreen('Play.JPG', confidence = 0.80).left+20
        InputY = pyautogui.locateOnScreen('Play.JPG', confidence = 0.80).top+30
        click(InputX, InputY)
        time.sleep(5)
        
if(pyautogui.locateOnScreen('EmailVerifyExit.JPG', confidence = 0.80)):
    InputX = pyautogui.locateOnScreen('EmailVerifyExit.JPG', confidence = 0.80).left+20
    InputY = pyautogui.locateOnScreen('EmailVerifyExit.JPG', confidence = 0.80).top+30
    click(InputX, InputY)
    time.sleep(1)

InputX = pyautogui.locateOnScreen('ClientPlay.JPG', confidence = 0.95).left+20
InputY = pyautogui.locateOnScreen('ClientPlay.JPG', confidence = 0.95).top+30
click(InputX, InputY)

while (pyautogui.locateOnScreen('Ranked.JPG', confidence = 0.95)) == None:
    time.sleep(1)

InputX = pyautogui.locateOnScreen('Ranked.JPG', confidence = 0.95).left+20
InputY = pyautogui.locateOnScreen('Ranked.JPG', confidence = 0.95).top+10
click(InputX, InputY)

while (pyautogui.locateOnScreen('Confirm.JPG', confidence = 0.95)) == None:
    time.sleep(1)

InputX = pyautogui.locateOnScreen('Confirm.JPG', confidence = 0.95).left+20
InputY = pyautogui.locateOnScreen('Confirm.JPG', confidence = 0.95).top+10
click(InputX, InputY)

if (role1 != "fill"):
    while (pyautogui.locateOnScreen('RoleSelect.JPG', confidence = 0.70)) == None:
        time.sleep(0.0000001)
    InputX = pyautogui.locateOnScreen('RoleSelect.JPG', confidence = 0.70).left+20
    InputY = pyautogui.locateOnScreen('RoleSelect.JPG', confidence = 0.70).top+10
    click(InputX, InputY)
    time.sleep(1)
    InputX = pyautogui.locateOnScreen('bot.JPG', confidence = 0.80).left+20
    InputY = pyautogui.locateOnScreen('bot.JPG', confidence = 0.80).top+10
    click(InputX, InputY)
    time.sleep(2)
    while (pyautogui.locateOnScreen('RoleSelect.JPG', confidence = 0.70)) == None:
        time.sleep(0.0000001)
    InputX = pyautogui.locateOnScreen('RoleSelect.JPG', confidence = 0.70).left+20
    InputY = pyautogui.locateOnScreen('RoleSelect.JPG', confidence = 0.70).top+10
    click(InputX, InputY)
    time.sleep(1)
    InputX = pyautogui.locateOnScreen('mid.JPG', confidence = 0.80).left+20
    InputY = pyautogui.locateOnScreen('mid.JPG', confidence = 0.80).top+10
    click(InputX, InputY)
    time.sleep(2)

while( pyautogui.locateOnScreen('FindMatch.JPG', confidence = 0.80)) == None:
    time.sleep(0.0000001)
InputX = pyautogui.locateOnScreen('FindMatch.JPG', confidence = 0.80).left+20
InputY = pyautogui.locateOnScreen('FindMatch.JPG', confidence = 0.80).top+10
click(InputX, InputY)

while(pyautogui.locateOnScreen('QueueIndicator.JPG', confidence = 0.80)):
    time.sleep(0.0000001)
    while(pyautogui.locateOnScreen('Accept.JPG', confidence = 0.80)) == None:
        time.sleep(0.0000001)
    InputX = pyautogui.locateOnScreen('Accept.JPG', confidence = 0.80).left+20
    InputY = pyautogui.locateOnScreen('Accept.JPG', confidence = 0.80).top+10
    click(InputX, InputY)


