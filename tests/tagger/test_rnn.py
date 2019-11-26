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
from tests.tagger.base import assert_tags_equal


def test():
    assert_tags_equal(
        tagger=RNNTagger(),
        expected=[
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
        words=['необычные', 'дела'],
    )
