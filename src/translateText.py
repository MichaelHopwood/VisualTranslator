from translate import Translator
from nltk.tokenize import sent_tokenize, word_tokenize

# implemented to avoid 500 char query limit
def word_boundary(text, char_limit):
    char_tokens = []
    current_chunk = []
    current_length = 0

    for sentence in text:
        words = word_tokenize(sentence)

        for word in words:
            word_length = len(word)

            if current_length + word_length + len(current_chunk) <= char_limit:
                current_chunk.append(word)
                current_length += word_length
            else:
                char_tokens.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = word_length

    if current_chunk:
        char_tokens.append(' '.join(current_chunk))

    return char_tokens

def translate(text):
    translator= Translator(from_lang='es', to_lang='en')
    translation = ''

    # Loop through each sentence to translate
    sents = sent_tokenize(text)
    for i in sents:
        # Calculate each word boundary of 500 characters or less
        for j in word_boundary(sent_tokenize(i), 500):
            translation += " " + translator.translate(j)
    return translation
