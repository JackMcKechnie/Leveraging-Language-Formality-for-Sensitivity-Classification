import language_tool_python
import textstat

def spelling_and_grammar(sentence,tool):
    num_errors = len(tool.check(sentence))
    num_words = textstat.lexicon_count(sentence,removepunct=True)
    error_percentage = num_errors / num_words *100
    return error_percentage