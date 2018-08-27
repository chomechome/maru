import abc
from typing import Tuple, Iterator

from maru.tag import Tag
from maru.types import Text, Index, Indices

Tagged = Tuple[Index, Tag]


class ITagger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        pass
