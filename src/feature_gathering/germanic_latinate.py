import ety
from nltk.tokenize import RegexpTokenizer

def germanic_latinate(sentence):

    etymology = []
    for word in sentence:
        etymology.append(ety.origins(word,recursive=True))

    germanics = 0
    latins = 0
    for word in etymology:
        word = str(word)
        if word.count("ang") != 0:
            germanics += 1
        if word.count("enm") != 0:
            germanics += 1
        if word.count("lat") != 0:
            latins += 1

    if latins != 0 and germanics == 0:
        return 100
    if latins == 0 and germanics == 0:
        return -1
    else:
        return (latins/germanics)*100