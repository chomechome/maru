from maru.lemmatizer.abstract import ILemmatizer
from maru.tag import Tag
from maru.types import Word


class DummyLemmatizer(ILemmatizer):
    def lemmatize(self, word: Word, tag: Tag) -> Word:
        return word
