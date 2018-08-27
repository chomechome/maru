from typing import Optional

import pymorphy2

from maru.grammeme import Aspect

_ASPECT = {
    'perf': Aspect.PERFECT,
    'impf': Aspect.IMPERFECT,
}


def get_aspect(parse: pymorphy2.analyzer.Parse) -> Optional[Aspect]:
    return _ASPECT.get(parse.tag.aspect)
