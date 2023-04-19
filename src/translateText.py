from translate import Translator
from nltk.tokenize import sent_tokenize

def translate(text):
    translator= Translator(from_lang='es', to_lang='en')
    translation = ''

    # Loop through each sentence to translate
    sents = sent_tokenize(text)
    for i in sents:
        translation += translator.translate(i)
    return translation
