from typing import Sequence, Iterable, Dict

from maru.grammeme import PartOfSpeech
from maru.lemmatizer import ILemmatizer
from maru.morph import Morph
from maru.tag import Tag
from maru.tagger.abstract import ITagger
from maru.types import Index, Text

_UNKNOWN = Tag(pos=PartOfSpeech.UNKNOWN)


class Analyzer:
    def __init__(self,
                 taggers: Sequence[ITagger],
                 lemmatizer: ILemmatizer,
                 ):
        self._taggers = taggers
        self._lemmatizer = lemmatizer

    def analyze(self, text: Text) -> Iterable[Morph]:
        tags: Dict[Index, Tag] = {}

        length = len(text)
        indices = range(length)
        for tagger in self._taggers:
            tags.update(tagger.tag(text, indices))
            indices = [index for index in indices if index not in tags]
            if not indices:
                break

        lemmatizer = self._lemmatizer
        for index, word in enumerate(text):
            tag = tags.get(index, _UNKNOWN)
            lemma = lemmatizer.lemmatize(word, tag)
            yield Morph(word, lemma, tag)
