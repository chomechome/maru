import pytest

from maru.grammeme import PartOfSpeech, NumericalForm
from maru.tag import Tag
from maru.tagger import NumericalTagger
from tests.tagger.base import assert_tags_equal

_INTEGER = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.INTEGER)
_REAL = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.REAL)


def test_integer():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[
            (0, _INTEGER),
            (1, _INTEGER),
        ],
        words=['123', '51515'],
    )


def test_real():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[
            (0, _REAL),
            (1, _REAL),
        ],
        words=['123.1231', '1231,34555'],
    )


def test_indices():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[
            (0, _REAL),
            (2, _INTEGER),
        ],
        words=['1.1', '123', '567'],
        indices=[0, 2],
    )


@pytest.mark.skip('Numerical tagger does not support ranges yet')
def test_numerical_range():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[
            (0, _INTEGER),
            (1, _INTEGER),
            (2, _INTEGER),
        ],
        words=['16-18', '1942-1944', '2/3'],
    )


def test_non_numerical():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[],
        words=['', '  ', '!!!!', 'XV', 'unknown', '<<123>>', '23years'],
    )
