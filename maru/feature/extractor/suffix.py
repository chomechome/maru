from typing import Sequence

from maru.feature.extractor.abstract import IFeatureExtractor
from maru.types import FeatureVector, Word


class SuffixExtractor(IFeatureExtractor):
    def __init__(self, sizes: Sequence[int] = range(1, 4)):
        self._sizes = sorted(sizes)

    def extract(self, word: Word) -> FeatureVector:
        for size in self._sizes:
            suffix = word[-size:]
            if suffix == word:
                break
            yield (f'suffix:{suffix}', 1)
