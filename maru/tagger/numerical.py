import re
from typing import Iterator

from maru.grammeme import PartOfSpeech
from maru.grammeme.numform import NumericalForm
from maru.tag import Tag
from maru.tagger.abstract import ITagger, Tagged
from maru.types import Indices, Text

_REGEX = re.compile(
    rf'(?P<{NumericalForm.REAL}>\d+[.,/]\d+$)|'
    rf'(?P<{NumericalForm.INTEGER}>\d+$)|'
    rf'(?P<{NumericalForm.RANGE}>\d+[‑–—−-]\d+)'
)
_TAGS = {
    NumericalForm.REAL: Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.REAL),
    NumericalForm.INTEGER: Tag(
        pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.INTEGER
    ),
    NumericalForm.RANGE: Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.RANGE),
}


class NumericalTagger(ITagger):
    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        for index in indices:
            match = _REGEX.match(text[index])
            if match is not None:
                form = NumericalForm(match.lastgroup)
                yield index, _TAGS[form]
