from typing import Optional

import pymorphy2

from maru.grammeme import Animacy

_ANIMACY = {
    'anim': Animacy.ANIMATE,
    'inan': Animacy.INANIMATE,
}


def get_animacy(parse: pymorphy2.analyzer.Parse) -> Optional[Animacy]:
    return _ANIMACY.get(parse.tag.animacy)
