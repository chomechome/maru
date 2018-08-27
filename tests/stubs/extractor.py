from maru.feature.extractor import IFeatureExtractor
from maru.types import Word, FeatureVector


class LengthExtractor(IFeatureExtractor):
    def extract(self, word: Word) -> FeatureVector:
        yield (word, len(word))
