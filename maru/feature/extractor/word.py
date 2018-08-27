from maru.feature.extractor.abstract import IFeatureExtractor
from maru.types import Word, FeatureVector


class WordExtractor(IFeatureExtractor):
    def extract(self, word: Word) -> FeatureVector:
        yield (f'word:{word}', 1)
