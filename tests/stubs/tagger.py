from typing import Iterator

from maru.tag import Tag
from maru.tagger.abstract import ITagger, Tagged
from maru.types import Word, Text, Indices


class SingleWordTagger(ITagger):
    def __init__(self, word: Word, tag: Tag):
        self._word = word
        self._tag = tag

    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        for index in indices:
            if text[index] == self._word:
                yield index, self._tag
