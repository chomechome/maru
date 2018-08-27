from typing import Optional

import pymorphy2

from maru.grammeme import Case

_CASE = {
    'ablt': Case.INSTRUCTIVE,
    'acc2': Case.ACCUSATIVE,
    'accs': Case.ACCUSATIVE,
    'datv': Case.DATIVE,
    'gen1': Case.GENITIVE,
    'gen2': Case.GENITIVE,
    'gent': Case.GENITIVE,
    'loc1': Case.LOCATIVE,
    'loc2': Case.LOCATIVE,
    'loct': Case.LOCATIVE,
    'nomn': Case.NOMINATIVE,
    'voct': Case.NOMINATIVE,
}


def get_case(parse: pymorphy2.analyzer.Parse) -> Optional[Case]:
    return _CASE.get(parse.tag.case)
