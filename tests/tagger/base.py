from typing import Sequence

from maru.tagger.abstract import ITagger, Tagged
from maru.types import Indices, Word


def assert_tags_equal(
    tagger: ITagger,
    expected: Sequence[Tagged],
    words: Sequence[Word],
    indices: Indices = None,
):
    if indices is None:
        indices = range(len(words))

    assert expected == list(tagger.tag(words, indices))
