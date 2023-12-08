import pyautogui
import time

# Pausa o programa por 5 segundos para permitir a troca para a tela que deseja capturar
while (4):
    time.sleep(5)

    # Retorna a posição atual do cursor do mouse
    print(pyautogui.position())
