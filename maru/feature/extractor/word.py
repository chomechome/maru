from maru.feature.extractor.abstract import IFeatureExtractor
from maru.types import FeatureVector, Word


class WordExtractor(IFeatureExtractor):
    def extract(self, word: Word) -> FeatureVector:
        yield (f'word:{word}', 1)
