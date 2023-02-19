import pyautogui 
from threading import Thread
from pynput.mouse import Controller, Button
from time import sleep
from pynput.keyboard import KeyCode,Listener
delay=0.2
mouse=Controller()

res = pyautogui.locateOnScreen("image.png")
print(res)
pyautogui.moveTo(res)

class AutoClicker(Thread):
    clicking = False

    def run(self):
        try: 
            while True:
                    if AutoClicker.clicking:
                        res = pyautogui.locateOnScreen("image.png",confidence=0.8)
                        print(res)
                        pyautogui.moveTo(res)
                        mouse.click(Button.left)
                        if res is None:
                           res2 = pyautogui.locateOnScreen("image2.png",confidence=0.8)
                           pyautogui.moveTo(res2)
                           mouse.click(Button.left)
                           sleep(0.5)
                           if res2 is not None:
                              res3 = pyautogui.locateOnScreen("image3.png",confidence=0.8)
                              pyautogui.moveTo(res3)
                              mouse.click(Button.left)
                              sleep(0.5)

                    sleep(delay)
        except KeyboardInterrupt:
            pass

def keypress(key):
    if key == KeyCode(char="k"):
        AutoClicker.clicking=not AutoClicker.clicking


AutoClicker().start()

with Listener(on_press=keypress) as listener:
    listener.join()