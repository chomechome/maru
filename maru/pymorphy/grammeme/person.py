from typing import Optional

import pymorphy2

from maru.grammeme import Person

_PERSON = {
    '1per': Person.FIRST,
    '2per': Person.SECOND,
    '3per': Person.THIRD,
}


def get_person(parse: pymorphy2.analyzer.Parse) -> Optional[Person]:
    return _PERSON.get(parse.tag.person)
