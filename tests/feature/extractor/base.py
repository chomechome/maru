from maru.feature.extractor import IFeatureExtractor
from maru.types import FeatureVector, Word


def assert_extracted_features_equal(extractor: IFeatureExtractor,
                                    word: Word,
                                    features: FeatureVector,
                                    ):
    assert features == list(extractor.extract(word))
