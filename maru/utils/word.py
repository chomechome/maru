import re
import unicodedata

from maru.types import Word


def normalize(word: Word) -> Word:
    word = word.strip().lower().replace('_', ' ')
    word = re.sub('\d', 'D', word)
    word = word.replace('<emo>', '.')
    return word


def is_punctuation(word: Word) -> bool:
    return all(unicodedata.category(sym).startswith('P') for sym in word)


def is_cyrillic(word: Word) -> bool:
    return re.search('[а-яА-Я]', word) is not None
