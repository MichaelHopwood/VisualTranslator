import requests
import json

# Translator API

def translate(text):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=es&tl=en&dt=t&q=" + text
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        return result[0][0][0]
    else:
        return "Error: Unable to translate text"
