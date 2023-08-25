from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)

def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    minWord = ""
    maxWord = ""
    minLen = len(text)
    maxLen = 0
    splittedText = text.split()
    for word in splittedText:
        if len(word) < minLen:
            minWord = word
            minLen = len(word)
        if len(word) > maxLen:
            maxWord = word
            maxLen = len(word)
    if not minWord:
        minWord = None
    if not maxWord:
        maxWord = None
    return minWord, maxWord
