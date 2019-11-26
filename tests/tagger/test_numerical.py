from maru.grammeme import NumericalForm, PartOfSpeech
from maru.tag import Tag
from maru.tagger import NumericalTagger
from tests.tagger.base import assert_tags_equal

_INTEGER = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.INTEGER)
_REAL = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.REAL)
_RANGE = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.RANGE)


def test_integer():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[(0, _INTEGER), (1, _INTEGER)],
        words=['123', '51515'],
    )


def test_real():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[(0, _REAL), (1, _REAL), (2, _REAL)],
        words=['123.1231', '1231,34555', '2/3'],
    )


def test_indices():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[(0, _REAL), (2, _INTEGER)],
        words=['1.1', '123', '567'],
        indices=[0, 2],
    )


def test_numerical_range():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[(0, _RANGE), (1, _RANGE)],
        words=['16-18', '1942—1944'],
    )


def test_non_numerical():
    assert_tags_equal(
        tagger=NumericalTagger(),
        expected=[],
        words=['', '  ', '!!!!', 'XV', 'unknown', '<<123>>', '23years'],
    )
