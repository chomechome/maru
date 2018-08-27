from typing import Optional

import pymorphy2

from maru.grammeme import Degree

_DEGREE = {
    'COMP': Degree.COMPARATIVE,
    'ADVB': Degree.POSITIVE,
    'ADJF': Degree.POSITIVE,
    'ADJS': Degree.POSITIVE,
}


def get_degree(parse: pymorphy2.analyzer.Parse) -> Optional[Degree]:
    if 'Supr' in parse.tag:
        return Degree.POSITIVE
    return _DEGREE.get(parse.tag.POS)
