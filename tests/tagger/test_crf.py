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
from maru.tagger import CRFTagger
from tests.tagger.base import TaggerTest


@pytest.fixture(name='tagger', scope='session')
def create_tagger():
    return CRFTagger()


@pytest.mark.parametrize(
    'test',
    [
        TaggerTest(
            words=['настоящий', 'полковник'],
            tags=[
                (
                    0,
                    Tag(
                        pos=PartOfSpeech.ADJECTIVE,
                        case=Case.NOMINATIVE,
                        degree=Degree.POSITIVE,
                        gender=Gender.MASCULINE,
                        number=Number.SINGULAR,
                        variant=Variant.FULL,
                    ),
                ),
                (
                    1,
                    Tag(
                        pos=PartOfSpeech.NOUN,
                        animacy=Animacy.ANIMATE,
                        case=Case.NOMINATIVE,
                        gender=Gender.MASCULINE,
                        number=Number.SINGULAR,
                    ),
                ),
            ],
        ),
        TaggerTest(
            words=['настоящий', 'робот'],
            tags=[
                (
                    0,
                    Tag(
                        pos=PartOfSpeech.ADJECTIVE,
                        case=Case.NOMINATIVE,
                        degree=Degree.POSITIVE,
                        gender=Gender.MASCULINE,
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
                        gender=Gender.MASCULINE,
                        number=Number.SINGULAR,
                    ),
                ),
            ],
        ),
    ],
)
def test_crf(test, tagger):
    test.run(tagger)
