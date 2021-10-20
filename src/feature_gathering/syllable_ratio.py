import textstat

def syllable_ratio(sentence):
    syllable_count = textstat.syllable_count(sentence)
    word_count = textstat.lexicon_count(sentence,removepunct=True)
    return syllable_count / word_count