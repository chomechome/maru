import pytest

from maru.grammeme import NumericalForm, PartOfSpeech
from maru.tag import Tag
from maru.tagger import NumericalTagger
from tests.tagger.base import TaggerTest

_INTEGER = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.INTEGER)
_REAL = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.REAL)
_RANGE = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.RANGE)


@pytest.fixture(name='tagger', scope='session')
def create_tagger():
    return NumericalTagger()


@pytest.mark.parametrize(
    'test',
    [
        TaggerTest(
            words=['123', '51515', '777'],
            tags=[(0, _INTEGER), (1, _INTEGER), (2, _INTEGER)],
        ),
        TaggerTest(
            words=['123.1231', '1231,34555', '2/3'],
            tags=[(0, _REAL), (1, _REAL), (2, _REAL)],
        ),
        TaggerTest(
            words=['1.1', '123', '567'],
            tags=[(0, _REAL), (2, _INTEGER)],
            indices=[0, 2],
        ),
        TaggerTest(
            words=['1.1', '123', '567'],
            tags=[(1, _INTEGER), (2, _INTEGER)],
            indices=[1, 2],
        ),
        TaggerTest(
            words=['16-18', '1942—1944', '1'],
            tags=[(0, _RANGE), (1, _RANGE), (2, _INTEGER)],
        ),
        TaggerTest(
            words=[
                '',
                '  ',
                '!!!!',
                'XV',
                'unknown',
                '<<123>>',
                '23years',
                '-',
                '.',
                ',',
                ',1',
                '.2',
            ],
            tags=[],
        ),
    ],
)
def test_numerical(test, tagger):
    test.run(tagger)
