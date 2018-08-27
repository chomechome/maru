from maru.feature.extractor import StemExtractor

from tests.feature.extractor.base import assert_extracted_features_equal


def test_cuts():
    assert_extracted_features_equal(
        extractor=StemExtractor(cuts=[1, 2], min_length=1),
        word='tests',
        features=[
            ('stem:test', 1),
            ('stem:tes', 1),
        ],
    )


def test_min_length():
    assert_extracted_features_equal(
        extractor=StemExtractor(cuts=[1, 2], min_length=4),
        word='test',
        features=[],
    )


def test_cut_order():
    assert_extracted_features_equal(
        extractor=StemExtractor(cuts=[2, 3, 1], min_length=2),
        word='cuts',
        features=[
            ('stem:cut', 1),
            ('stem:cu', 1),
        ],
    )
