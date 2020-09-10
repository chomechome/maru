import pytest

from maru.grammeme import (
    Animacy,
    Case,
    Degree,
    Gender,
    Number,
    PartOfSpeech,
    Variant,
)
from maru.tag import Tag
from maru.tagger import RNNTagger
from tests.tagger.base import TaggerTest


@pytest.fixture(name='tagger', scope='session')
def create_tagger():
    return RNNTagger()


@pytest.mark.parametrize(
    'test',
    [
        TaggerTest(
            words=['необычные', 'дела'],
            tags=[
                (
                    0,
                    Tag(
                        pos=PartOfSpeech.ADJECTIVE,
                        case=Case.NOMINATIVE,
                        degree=Degree.POSITIVE,
                        number=Number.PLURAL,
                        variant=Variant.FULL,
                    ),
                ),
                (
                    1,
                    Tag(
                        pos=PartOfSpeech.NOUN,
                        animacy=Animacy.INANIMATE,
                        case=Case.NOMINATIVE,
                        gender=Gender.NEUTER,
                        number=Number.PLURAL,
                    ),
                ),
            ],
        ),
        TaggerTest(
            words=['необычных', 'дел'],
            tags=[
                (
                    0,
                    Tag(
                        pos=PartOfSpeech.ADJECTIVE,
                        case=Case.GENITIVE,
                        degree=Degree.POSITIVE,
                        number=Number.PLURAL,
                        variant=Variant.FULL,
                    ),
                ),
                (
                    1,
                    Tag(
                        pos=PartOfSpeech.NOUN,
                        animacy=Animacy.INANIMATE,
                        case=Case.GENITIVE,
                        gender=Gender.NEUTER,
                        number=Number.PLURAL,
                    ),
                ),
            ],
        ),
    ],
)
def test_rnn(test, tagger):
    test.run(tagger)
