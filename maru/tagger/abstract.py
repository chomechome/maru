import abc
from typing import Iterator, Tuple

from maru.tag import Tag
from maru.types import Index, Indices, Text

Tagged = Tuple[Index, Tag]


class ITagger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        pass
