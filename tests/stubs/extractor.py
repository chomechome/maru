from maru.feature.extractor import IFeatureExtractor
from maru.types import FeatureVector, Word


class LengthExtractor(IFeatureExtractor):
    def extract(self, word: Word) -> FeatureVector:
        yield (word, len(word))
