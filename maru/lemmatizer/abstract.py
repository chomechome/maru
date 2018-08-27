import abc

from maru.tag import Tag
from maru.types import Word


class ILemmatizer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lemmatize(self, word: Word, tag: Tag) -> Word:
        pass
