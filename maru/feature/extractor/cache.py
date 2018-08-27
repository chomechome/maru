import lru
from typing import Tuple

from maru.feature.extractor.abstract import IFeatureExtractor
from maru.types import Word, FeatureVector


class Cache(IFeatureExtractor):
    def __init__(self, extractor: IFeatureExtractor, size: int):
        self._extractor = extractor
        self._cache = lru.LRU(size)

    def __getstate__(self) -> Tuple[IFeatureExtractor, int]:
        return self._extractor, self._cache.get_size()

    def __setstate__(self, state: Tuple[IFeatureExtractor, int]):
        extractor, size = state
        self._extractor = extractor
        self._cache = lru.LRU(size)

    def extract(self, word: Word) -> FeatureVector:
        cache = self._cache
        if word not in cache:
            cache[word] = list(self._extractor.extract(word))
        return cache[word]
