from typing import Iterator

from maru.grammeme import PartOfSpeech
from maru.tag import Tag
from maru.tagger.abstract import ITagger, Tagged
from maru.types import Indices, Text
from maru.utils.word import is_punctuation

_PUNCTUATION = Tag(pos=PartOfSpeech.PUNCTUATION)


class PunctuationTagger(ITagger):
    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        for index in indices:
            word = text[index].strip()
            if word and is_punctuation(word):
                yield index, _PUNCTUATION
