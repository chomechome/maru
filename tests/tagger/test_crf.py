from maru.grammeme import (
    PartOfSpeech,
    Animacy,
    Case,
    Gender,
    Number,
    Degree,
    Variant,
)
from maru.tag import Tag
from maru.tagger import CRFTagger

from tests.tagger.base import assert_tags_equal


def test():
    assert_tags_equal(
        tagger=CRFTagger(),
        expected=[
            (
                0,
                Tag(
                    pos=PartOfSpeech.ADJECTIVE,
                    case=Case.NOMINATIVE,
                    degree=Degree.POSITIVE,
                    gender=Gender.MASCULINE,
                    number=Number.SINGULAR,
                    variant=Variant.FULL,
                )
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
        words=['настоящий', 'детектив'],
    )
