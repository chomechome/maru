import pymorphy2.analyzer

from maru.pymorphy.grammeme import (
    get_animacy,
    get_aspect,
    get_case,
    get_degree,
    get_gender,
    get_mood,
    get_number,
    get_part_of_speech,
    get_person,
    get_tense,
    get_verbform,
    get_voice,
)
from maru.tag import Tag


def get_tag(parse: pymorphy2.analyzer.Parse) -> Tag:
    return Tag(
        pos=get_part_of_speech(parse),
        animacy=get_animacy(parse),
        aspect=get_aspect(parse),
        case=get_case(parse),
        degree=get_degree(parse),
        gender=get_gender(parse),
        mood=get_mood(parse),
        number=get_number(parse),
        person=get_person(parse),
        tense=get_tense(parse),
        verbform=get_verbform(parse),
        voice=get_voice(parse),
    )
