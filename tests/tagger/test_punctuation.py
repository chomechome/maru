import pytest

from maru.grammeme import PartOfSpeech
from maru.tag import Tag
from maru.tagger.punctuation import PunctuationTagger
from tests.tagger.base import assert_tags_equal

_PUNCTUATION = Tag(pos=PartOfSpeech.PUNCTUATION)


@pytest.mark.parametrize(
    ['word'],
    [
        ['!'],
        ['@'],
        ['.....,'],
        ['?!'],
        ['"'],
        [':'],
        [';'],
        ['()'],
        ['%'],
    ]
)
def test_punctuation(word: str):
    assert_tags_equal(
        tagger=PunctuationTagger(),
        expected=[
            (0, _PUNCTUATION),
        ],
        words=[word],
    )


@pytest.mark.parametrize(
    ['word'],
    [
        ['12313'],
        ['unknown'],
        ['XV'],
        ['   '],
        [''],
    ]
)
def test_non_punctuation(word: str):
    assert_tags_equal(
        tagger=PunctuationTagger(),
        expected=[],
        words=[word],
    )


def test_indices():
    assert_tags_equal(
        tagger=PunctuationTagger(),
        expected=[
            (1, _PUNCTUATION),
            (2, _PUNCTUATION),
        ],
        words=['?', ',', '!'],
        indices=[1, 2],
    )
