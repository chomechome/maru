from typing import Optional

import pymorphy2

from maru.grammeme import Voice

_VOICE = {
    'actv': Voice.ACTIVE,
    'pssv': Voice.PASSIVE,
}


def get_voice(parse: pymorphy2.analyzer.Parse) -> Optional[Voice]:
    return _VOICE.get(parse.tag.voice)
