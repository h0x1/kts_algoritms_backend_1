from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)

def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    minWord = "None"
    maxWord = "None"
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
    return minWord, maxWord
