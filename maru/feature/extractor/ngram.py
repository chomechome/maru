from typing import Sequence

from maru.feature.extractor import IFeatureExtractor
from maru.types import FeatureVector, Word


class NGramExtractor(IFeatureExtractor):
    def __init__(self, sizes: Sequence[int] = range(2, 6)):
        self._sizes = sizes

    def extract(self, word: Word) -> FeatureVector:
        word = f'<{word}>'

        length = len(word)
        for size in self._sizes:
            for start in range(length - size + 1):
                yield (f'ngram:{word[start: start + size]}', 1)
