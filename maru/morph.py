from typing import NamedTuple

from maru.tag import Tag
from maru.types import Word


class Morph(NamedTuple):
    word: Word
    lemma: Word
    tag: Tag
