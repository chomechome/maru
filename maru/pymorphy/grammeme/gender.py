from typing import Optional

import pymorphy2

from maru.grammeme import Gender

_GENDER = {
    'femn': Gender.FEMININE,
    'masc': Gender.MASCULINE,
    'neut': Gender.NEUTER,
}


def get_gender(parse: pymorphy2.analyzer.Parse) -> Optional[Gender]:
    return _GENDER.get(parse.tag.gender)
