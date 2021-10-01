import nltk


def f_score(sentence):

    tokens = nltk.word_tokenize(sentence)
    pos = nltk.pos_tag(tokens)

    f_count = 0
    c_count = 0

    # Nouns, adjectives, prepositions and articles. Does not yet include articles.
    f_types = ["NN", "NNS", "JJ", "JJR", "JJS", "IN"]
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



