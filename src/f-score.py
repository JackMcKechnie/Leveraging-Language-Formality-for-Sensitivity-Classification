import nltk
from nltk.tokenize import RegexpTokenizer


def f_score(sentence):

    #Remove punctuation from the sentence when tokenising
    tokenizer = RegexpTokenizer(r'\w+')
    sentence = tokenizer.tokenize(sentence)    
    pos = nltk.pos_tag(sentence)

    f_count = 0
    c_count = 0

    # Nouns, adjectives, prepositions and articles.
    f_types = ["NN", "NNS", "JJ", "JJR", "JJS", "IN","DET"]
    #Pronouns, verbs, adverbs and interjections
    c_types = ["PRP", "PRP$", "WP", "WP$", "VB", "VBD",
               "VBG", "VBN", "VBP", "VBZ", "RB", "RBR", "RBS", "UH"]

    for point in pos:
        if point[1] in f_types:
            f_count += 1
        if point[1] in c_types:
            c_count += 1

    f_score = (f_count - c_count + 100) / 2
    
    return f_score


