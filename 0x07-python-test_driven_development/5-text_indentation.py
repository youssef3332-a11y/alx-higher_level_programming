#!/usr/bin/python3
"""module:
metriser les tests
"""
def text_indentation(text):
    """module:
    Args: text
    Raises: TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ('.', '?', ':'):
            print("\n")
            if text[i + 1] == ' ':
                i+=1
        i+=1
