from translate import Translator

def translate(text):
    translator= Translator(from_lang='es', to_lang='en')
    translation = translator.translate(text)
    return translation
