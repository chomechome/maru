from typing import Tuple

import lru

from maru.lemmatizer.abstract import ILemmatizer
from maru.tag import Tag
from maru.types import Word


class Cache(ILemmatizer):
    def __init__(self, lemmatizer: ILemmatizer, size: int):
        self._lemmatizer = lemmatizer

        self._cache = lru.LRU(size)

    def __getstate__(self) -> Tuple[ILemmatizer, int]:
        return self._lemmatizer, self._cache.get_size()

    def __setstate__(self, state: Tuple[ILemmatizer, int]):
        lemmatizer, size = state
        self._lemmatizer = lemmatizer
        self._cache = lru.LRU(size)

    def lemmatize(self, word: Word, tag: Tag) -> Word:
        key = word, tag
        cache = self._cache
        if key not in cache:
            cache[key] = self._lemmatizer.lemmatize(word, tag)
        return cache[key]
