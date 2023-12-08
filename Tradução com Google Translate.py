from translate import Translator

translator = Translator(to_lang='pt')
texto = "Hello, how are you?"

traducao = translator.translate(texto)

print(traducao)  # Saída: "Hello, how are you?"
