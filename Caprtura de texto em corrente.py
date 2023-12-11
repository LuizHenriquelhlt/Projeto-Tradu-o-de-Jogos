import pyautogui
import pytesseract
from googletrans import Translator

# Função para capturar o texto na posição (x, y) da tela
def capturar_texto(x, y, width, height):
    return pyautogui.screenshot(region=(x, y, width, height))

# Função para traduzir o texto usando Google Translate
def traduzir_texto(texto):
    translator = Translator()
    traducao = translator.translate(texto, dest='pt')  # 'pt' para português, ajuste conforme necessário
    return traducao.text

# Coordenadas da área da tela onde está o diálogo
# Essas coordenadas precisam ser ajustadas para capturar somente a caixa de diálogo do NPC
x_caixa_dialogo = 47
y_caixa_dialogo = 726
largura_caixa_dialogo = 1768
altura_caixa_dialogo = 36

# Capturando a caixa de diálogo como uma imagem
imagem_dialogo = capturar_texto(x_caixa_dialogo, y_caixa_dialogo, largura_caixa_dialogo, altura_caixa_dialogo)

# Convertendo a imagem para texto usando OCR (Reconhecimento Óptico de Caracteres)
texto_caixa_dialogo = pytesseract.image_to_string(imagem_dialogo)

# Traduzindo o texto para o português
texto_traduzido = traduzir_texto(texto_caixa_dialogo)

# Exibindo o texto traduzido
print("Texto original:", texto_caixa_dialogo)
print("Texto traduzido:", texto_traduzido)
