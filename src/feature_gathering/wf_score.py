import nltk
from nltk.tokenize import RegexpTokenizer

def wf_score(sentence):
    pos = nltk.pos_tag(sentence)

    noun_tags = ["NN","NNS","NNP","NNPS"]
    adjective_tags = ["JJ","JJR","JJS"]
    article_tags = ["DT"]
    pronoun_tags = ["PRP","PRP$","WP","WP$"]
    verb_tags = ["VB","VBD","VBG","VBN","VBP","VBZ"]

    noun_count = 0
    adjective_count = 0
    article_count = 0
    pronoun_count = 0
    verb_count = 0

    for point in pos:
        point = point[1]
        if point in noun_tags:
            noun_count += 1
        if point in adjective_tags:
            adjective_count += 1
        if point in article_tags:
            article_count += 1
        if point in pronoun_tags:
            pronoun_count += 1
        if point in verb_tags:
            pronoun_count += 1

    wf_score = 4.9717 + 0.0264 * noun_count + 0.0617 * adjective_count - 0.0742 * article_count - 0.0729 * pronoun_count - 0.0441 * verb_count

    return(wf_score)

