from typing import List

import lru
import pymorphy2.analyzer

from maru.types import Word

_ANALYZER = pymorphy2.MorphAnalyzer()
_CACHE = lru.LRU(15000)


def analyze(word: Word) -> List[pymorphy2.analyzer.Parse]:
    cache = _CACHE
    if word not in cache:
        cache[word] = _ANALYZER.parse(word)
    return cache[word]


def set_cache_size(size: int):
    _CACHE.set_size(size)
