from maru.feature.extractor import WordExtractor

from tests.feature.extractor.base import assert_extracted_features_equal


def test():
    assert_extracted_features_equal(
        extractor=WordExtractor(),
        word='test',
        features=[
            ('word:test', 1),
        ],
    )
