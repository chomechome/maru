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
from maru.tagger import LinearTagger
from tests.tagger.base import TaggerTest


@pytest.fixture(name='tagger', scope='session')
def create_tagger():
    return LinearTagger()


@pytest.mark.parametrize(
    'test',
    [
        TaggerTest(
            words=['чёрное', 'зеркало'],
            tags=[
                (
                    0,
                    Tag(
                        pos=PartOfSpeech.ADJECTIVE,
                        case=Case.NOMINATIVE,
                        degree=Degree.POSITIVE,
                        gender=Gender.NEUTER,
                        number=Number.SINGULAR,
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
                        number=Number.SINGULAR,
                    ),
                ),
            ],
        ),
        TaggerTest(
            words=['чёрного', 'зеркала'],
            tags=[
                (
                    0,
                    Tag(
                        pos=PartOfSpeech.ADJECTIVE,
                        case=Case.GENITIVE,
                        degree=Degree.POSITIVE,
                        gender=Gender.NEUTER,
                        number=Number.SINGULAR,
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
                        number=Number.SINGULAR,
                    ),
                ),
            ],
        ),
    ],
)
def test_linear(test, tagger):
    test.run(tagger)
