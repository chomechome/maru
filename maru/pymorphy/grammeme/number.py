from typing import Optional

import pymorphy2

from maru.grammeme import Number

_NUMBER = {
    'sing': Number.SINGULAR,
    'plur': Number.PLURAL,
}


def get_number(parse: pymorphy2.analyzer.Parse) -> Optional[Number]:
    return _NUMBER.get(parse.tag.number)
