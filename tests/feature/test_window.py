from typing import Iterable

import pytest

from maru.feature.window import FeatureWindowGenerator, FeatureWindow
from maru.types import Text, Indices

from tests.stubs.extractor import LengthExtractor


@pytest.fixture(name='extractor')
def _get_extractor():
    return LengthExtractor()


def _assert_windows_equal(expected: Iterable[FeatureWindow],
                          generator: FeatureWindowGenerator,
                          text: Text,
                          indices: Indices = None,
                          ):
    actual = generator.generate(text, indices or range(len(text)))

    def unroll(windows: Iterable[FeatureWindow]):
        return [
            [(position, list(features)) for position, features in window]
            for window in windows
        ]

    expected = unroll(expected)
    actual = unroll(actual)

    assert len(expected) == len(actual)
    for expected_window, actual_window in zip(expected, actual):
        assert expected_window == actual_window


def test_generate(extractor: LengthExtractor):
    generator = FeatureWindowGenerator(
        extractors={offset: extractor for offset in range(-1, 2)}
    )

    text = ['мама', 'мыла', 'раму']
    expected = [
        [
            (0, [('мама', 4)]),
            (1, [('мыла', 4)]),
        ],
        [
            (-1, [('мама', 4)]),
            (0, [('мыла', 4)]),
            (1, [('раму', 4)]),
        ],
        [
            (-1, [('мыла', 4)]),
            (0, [('раму', 4)]),
        ],
    ]

    _assert_windows_equal(expected, generator, text)


def test_generate_from_single_word(extractor: LengthExtractor):
    generator = FeatureWindowGenerator(
        extractors={offset: extractor for offset in range(-2, 3)}
    )

    text = ['мама']
    expected = [
        [
            (0, [('мама', 4)]),
        ],
    ]

    _assert_windows_equal(expected, generator, text)


def test_generate_with_indices(extractor: LengthExtractor):
    generator = FeatureWindowGenerator(
        extractors={offset: extractor for offset in range(-2, 3)}
    )

    text = ['раз', 'два', 'три']
    expected = [
        [
            (-1, [('раз', 3)]),
            (0, [('два', 3)]),
            (1, [('три', 3)]),
        ],
        [
            (-2, [('раз', 3)]),
            (-1, [('два', 3)]),
            (0, [('три', 3)]),
        ],
    ]

    _assert_windows_equal(expected, generator, text, indices=[1, 2])
