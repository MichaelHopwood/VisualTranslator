import easyocr

reader = easyocr.Reader(['es']) # this needs to run only once to load the model into memory

def read(image):
    result = reader.readtext(image, detail = 0)
    result = " ".join(result)
    return result