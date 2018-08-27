from typing import Iterator

from maru import pymorphy
from maru.tagger import ITagger
from maru.tagger.abstract import Tagged
from maru.types import Indices, Text


class PymorphyTagger(ITagger):
    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        for index in indices:
            parse = pymorphy.analyze(text[index])[0]
            tag = pymorphy.get_tag(parse)
            yield index, tag
