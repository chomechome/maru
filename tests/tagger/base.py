from typing import NamedTuple, Optional, Sequence

from maru.tagger.abstract import ITagger, Tagged
from maru.types import Indices, Word


class TaggerTest(NamedTuple):
    words: Sequence[Word]
    tags: Sequence[Tagged]
    indices: Optional[Indices] = None

    def run(self, tagger: ITagger):
        indices = self.indices
        if indices is None:
            indices = range(len(self.words))

        assert self.tags == list(tagger.tag(self.words, indices))
