# Summarize english passage

def summarize(text):
    
    #Libraries
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize

    #Data download (might need)
    nltk.download('stopwords')
    nltk.download('punkt')
    
    #Tokenize words and sentences, set up stopwords
    stoppers = set(stopwords.words("english"))
    words = word_tokenize(text)
    sents = sent_tokenize(text)

    #Create dictionary to track word scores
    wordScores = dict()
    
    #For loop to tally word scores
    for i in words:
        i = i.lower()
        if i in stoppers:
            continue
        if i in wordScores:
            wordScores[i] += 1
        else:
            wordScores[i] = 1

    #Create dictionary to track sentence scores
    sentenceScores = dict()
       
    #For loop to tally sentence scores
    for j in sents:
        for i, count in wordScores.items():
            if i in j.lower():
                if j in sentenceScores:
                    sentenceScores[j] += count
                else:
                    sentenceScores[j] = count
      
    #Initialize sum
    sentenceScoresSum = 0
    
    #Tally sum
    for j in sentenceScores:
        sentenceScoresSum += sentenceScores[j]
       
    #Initialize summary
    summary_text = ''
    
    #Build summary
    for j in sents:
        if (j in sentenceScores) and (sentenceScores[j] > (1.2 * (int(sentenceScoresSum / len(sentenceScores))))):
            summary_text += " " + j

    return print(summary_text)
