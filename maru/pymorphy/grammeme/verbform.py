from typing import Optional

import pymorphy2

from maru.grammeme import VerbForm

_VERBFORM = {
    'INFN': VerbForm.INFINITIVE,
    'VERB': VerbForm.FINITE,
    'GRND': VerbForm.CONVERB,
}


def get_verbform(parse: pymorphy2.analyzer.Parse) -> Optional[VerbForm]:
    return _VERBFORM.get(parse.tag.POS)
