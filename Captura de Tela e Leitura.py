import pyautogui
import pytesseract


# Coordenadas em relação ao segundo monitor
x = -669  # Coordenada X no segundo monitor
y = 95    # Coordenada Y no segundo monitor
width = 583  # Largura da área a ser capturada
height = 966 # Altura da área a ser capturada

# Captura uma área do segundo monitor onde o texto está presente
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# Usa o pytesseract para reconhecer o texto na imagem capturada
texto = pytesseract.image_to_string(screenshot)

print(texto)
