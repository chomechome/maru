import re
from typing import Iterator

from maru.grammeme import PartOfSpeech
from maru.grammeme.numform import NumericalForm
from maru.tag import Tag
from maru.tagger.abstract import ITagger, Tagged
from maru.types import Text, Indices

_REGEX = re.compile(f'(?P<{NumericalForm.REAL}>\d+[.,]\d+$)|'
                    f'(?P<{NumericalForm.INTEGER}>\d+$)')

_INTEGER = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.INTEGER)
_REAL = Tag(pos=PartOfSpeech.NUMERICAL, numform=NumericalForm.REAL)


class NumericalTagger(ITagger):
    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        for index in indices:
            match = _REGEX.match(text[index])
            if match is not None:
                group = match.lastgroup
                tag = _REAL if group == NumericalForm.REAL else _INTEGER
                yield index, tag
