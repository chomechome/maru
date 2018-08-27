from typing import Iterator

from maru import pymorphy
from maru.tag import Tag
from maru.tagger import ITagger
from maru.tagger.abstract import Tagged
from maru.types import Indices, Text


class PymorphyTagger(ITagger):
    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        for index in indices:
            parse = pymorphy.analyze(text[index])[0]
            tag = Tag(
                pos=pymorphy.get_part_of_speech(parse),
                animacy=pymorphy.get_animacy(parse),
                aspect=pymorphy.get_aspect(parse),
                case=pymorphy.get_case(parse),
                degree=pymorphy.get_degree(parse),
                gender=pymorphy.get_gender(parse),
                mood=pymorphy.get_mood(parse),
                number=pymorphy.get_number(parse),
                person=pymorphy.get_person(parse),
                tense=pymorphy.get_tense(parse),
                verbform=pymorphy.get_verbform(parse),
                voice=pymorphy.get_voice(parse),
            )
            yield index, tag
