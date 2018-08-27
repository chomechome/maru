from maru.feature.extractor import IFeatureExtractor
from maru.types import Word, FeatureVector


class OneHotExtractor(IFeatureExtractor):
    def __init__(self, extractor: IFeatureExtractor):
        self._extractor = extractor

    def extract(self, word: Word) -> FeatureVector:
        for name, value in self._extractor.extract(word):
            yield (f'{name}:{value}', 1)
