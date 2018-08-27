from typing import Optional

import pymorphy2

from maru.grammeme import Mood

_MOOD = {
    'indc': Mood.INDICATIVE,
    'impr': Mood.IMPERATIVE,
}


def get_mood(parse: pymorphy2.analyzer.Parse) -> Optional[Mood]:
    return _MOOD.get(parse.tag.mood)
