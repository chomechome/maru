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
from tests.tagger.base import assert_tags_equal


def test():
    assert_tags_equal(
        tagger=LinearTagger(),
        expected=[
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
        words=['чёрное', 'зеркало'],
    )
