from maru.feature.extractor import SuffixExtractor

from tests.feature.extractor.base import assert_extracted_features_equal


def test_sizes():
    assert_extracted_features_equal(
        extractor=SuffixExtractor(sizes=[1, 2]),
        word='test',
        features=[
            ('suffix:t', 1),
            ('suffix:st', 1),
        ],
    )


def test_whole_word_is_not_a_suffix():
    assert_extracted_features_equal(
        extractor=SuffixExtractor(sizes=[4]),
        word='test',
        features=[],
    )


def test_size_order():
    assert_extracted_features_equal(
        extractor=SuffixExtractor(sizes=[4, 1]),
        word='test',
        features=[
            ('suffix:t', 1),
        ],
    )
