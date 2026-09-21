import time
import pyautogui

# o tempo necessário para escolher aonde vai ser a posição desejada.
time.sleep(5)
# vai mostrar a posição do mouse na tela escolhida.
print(pyautogui.position())

pyautogui.scroll(200)
