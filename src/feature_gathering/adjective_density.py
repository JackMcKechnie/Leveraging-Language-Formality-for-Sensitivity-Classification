import nltk
from nltk.tokenize import RegexpTokenizer


def adjective_density(sentence):

    #Remove punctuation from the sentence when tokenising
    tokenizer = RegexpTokenizer(r'\w+')
    sentence = tokenizer.tokenize(sentence)

    #Extract points of speech
    pos = nltk.pos_tag(sentence)

    adjective_count = 0

    #NLTK adjectvie labels
    adjective_types = ["JJ", "JJR", "JJS"]

    #Get frequency of adjectives 
    for point in pos:
        if point[1] in adjective_types:
            adjective_count += 1

    #Calculate adjective density
    adjective_density = (adjective_count / len(sentence)) * 100

    return adjective_density

