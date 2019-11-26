from typing import Iterable, List, Tuple

import pytest

from maru.feature.window import FeatureWindow, FeatureWindowGenerator
from maru.types import Feature, Indices, Offset, Text
from tests.stubs.extractor import LengthExtractor


@pytest.fixture(name='extractor')
def _get_extractor():
    return LengthExtractor()


def _unroll(
    windows: Iterable[FeatureWindow],
) -> List[List[Tuple[Offset, List[Feature]]]]:
    return [
        [(position, list(features)) for position, features in window]
        for window in windows
    ]


def _assert_windows_equal(
    expected: Iterable[FeatureWindow],
    generator: FeatureWindowGenerator,
    text: Text,
    indices: Indices = None,
):
    actual = generator.generate(text, indices or range(len(text)))

    expected = _unroll(expected)
    actual = _unroll(actual)

    assert len(expected) == len(actual)
    for expected_window, actual_window in zip(expected, actual):
        assert expected_window == actual_window


def test_generate(extractor: LengthExtractor):
    generator = FeatureWindowGenerator(
        extractors={offset: extractor for offset in range(-1, 2)}
    )

    text = ['мама', 'мыла', 'раму']
    expected = [
        [(0, [('мама', 4)]), (1, [('мыла', 4)])],
        [(-1, [('мама', 4)]), (0, [('мыла', 4)]), (1, [('раму', 4)])],
        [(-1, [('мыла', 4)]), (0, [('раму', 4)])],
    ]

    _assert_windows_equal(expected, generator, text)


def test_generate_from_single_word(extractor: LengthExtractor):
    generator = FeatureWindowGenerator(
        extractors={offset: extractor for offset in range(-2, 3)}
    )

    text = ['мама']
    expected = [
        [(0, [('мама', 4)])],
    ]

    _assert_windows_equal(expected, generator, text)


def test_generate_with_indices(extractor: LengthExtractor):
    generator = FeatureWindowGenerator(
        extractors={offset: extractor for offset in range(-2, 3)}
    )

    text = ['раз', 'два', 'три']
    expected = [
        [(-1, [('раз', 3)]), (0, [('два', 3)]), (1, [('три', 3)])],
        [(-2, [('раз', 3)]), (-1, [('два', 3)]), (0, [('три', 3)])],
    ]

    _assert_windows_equal(expected, generator, text, indices=[1, 2])
