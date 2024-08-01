#Text Translation
from googletrans import Translator

def translate_text():
    print("Welcome to the Text Translation Script!")
    text = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., 'es' for Spanish): ")

    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    print(f"Translated text: {translated.text}")

if __name__ == "__main__":
    translate_text()
