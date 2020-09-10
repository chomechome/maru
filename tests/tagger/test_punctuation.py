import pytest

from maru.grammeme import PartOfSpeech
from maru.tag import Tag
from maru.tagger.punctuation import PunctuationTagger
from tests.tagger.base import TaggerTest

_PUNCTUATION = Tag(pos=PartOfSpeech.PUNCTUATION)


@pytest.fixture(name='tagger', scope='session')
def create_tagger():
    return PunctuationTagger()


@pytest.mark.parametrize(
    'test',
    [
        TaggerTest(
            words=['!', '@', '.....,'],
            tags=[(0, _PUNCTUATION), (1, _PUNCTUATION), (2, _PUNCTUATION)],
        ),
        TaggerTest(
            words=['?!', '"', ':', ';'],
            tags=[
                (0, _PUNCTUATION),
                (1, _PUNCTUATION),
                (2, _PUNCTUATION),
                (3, _PUNCTUATION),
            ],
        ),
        TaggerTest(words=['()', '%'], tags=[(0, _PUNCTUATION), (1, _PUNCTUATION)],),
        TaggerTest(
            words=['?', ',', '!'],
            tags=[(1, _PUNCTUATION), (2, _PUNCTUATION)],
            indices=[1, 2],
        ),
        TaggerTest(words=['12313', 'unknown', 'XV', '   ', ''], tags=[],),
    ],
)
def test_punctuation(test, tagger):
    test.run(tagger)
