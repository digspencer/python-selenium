import pyautogui
import time

conectar = pyautogui.locateOnScreen('conectar.png')
enviar = pyautogui.locateOnScreen('enviar.png')
avancar = pyautogui.locateOnScreen('avançar.png')

while True:
    if conectar:
        pyautogui.click('conectar.png')
        time.sleep(1)
        pyautogui.click('enviar.png')
    elif avancar:
        pyautogui.click('avançar.png')
    else:
        num_rolagem = 5
        for n in range(num_rolagem):
            pyautogui.scroll(-50)