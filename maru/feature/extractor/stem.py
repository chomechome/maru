from typing import Sequence

from maru.feature.extractor import IFeatureExtractor
from maru.types import FeatureVector, Word


class StemExtractor(IFeatureExtractor):
    def __init__(self, cuts: Sequence[int] = range(1, 4), min_length: int = 3):
        self._cuts = sorted(cuts)
        self._min_length = min_length

    def extract(self, word: Word) -> FeatureVector:
        length = len(word)
        for cut in self._cuts:
            if length - cut < self._min_length:
                break

            yield (f'stem:{word[:-cut]}', 1)
