from typing import Optional

import pymorphy2

from maru.grammeme import Tense

_TENSE = {
    'pres': Tense.PRESENT,
    'past': Tense.PAST,
    'futr': Tense.FUTURE,
}


def get_tense(parse: pymorphy2.analyzer.Parse) -> Optional[Tense]:
    return _TENSE.get(parse.tag.tense)
