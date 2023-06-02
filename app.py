import pyautogui
import time

conectar = pyautogui.locateOnScreen('conectar.png')
seguir = pyautogui.locateOnScreen('enviar.png')

while not conectar:
    time.sleep(1)
    pyautogui.scroll(-50)
    if conectar:
        pyautogui.click('conectar.png')
        time.sleep(1)
        pyautogui.click('enviar.png')
    elif pyautogui.locateOnScreen('avançar.png'):
            pyautogui.click('avançar.png')
