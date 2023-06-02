import pyautogui
import time

conectar = pyautogui.locateOnScreen('conectar.png')
seguir = pyautogui.locateOnScreen('enviar.png')
avancar = pyautogui.locateOnScreen('avançar.png')

def Se_conectar():
        if conectar:
            time.sleep(1)
            pyautogui.click('conectar.png')
            time.sleep(1)
            pyautogui.click('enviar.png')
        else:
            pyautogui.scroll(-50)



Se_conectar()