from typing import Sequence

from maru.feature.extractor.abstract import IFeatureExtractor
from maru.types import Word, FeatureVector


class Pipeline(IFeatureExtractor):
    def __init__(self, extractors: Sequence[IFeatureExtractor]):
        self._extractors = extractors

    def extract(self, word: Word) -> FeatureVector:
        for extractor in self._extractors:
            yield from extractor.extract(word)
