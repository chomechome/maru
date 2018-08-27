from typing import Iterable

from maru.tagger import (
    ITagger,
    PymorphyTagger,
    LinearTagger,
    CRFTagger,
    RNNTagger,
)


def get_tagger(name: str, cache_size: int) -> ITagger:
    taggers = {
        'pymorphy': lambda: PymorphyTagger(),
        'linear': lambda: LinearTagger(cache_size=cache_size),
        'crf': lambda: CRFTagger(cache_size=cache_size),
        'rnn': lambda: RNNTagger(cache_size=cache_size),
    }
    if name not in taggers:
        raise InvalidTaggerError(name, taggers)

    return taggers[name]()


class InvalidTaggerError(Exception):
    def __init__(self, tagger: str, expected: Iterable[str]):
        super().__init__(f'Invalid tagger {tagger}. '
                         f'Valid taggers are: {", ".join(expected)}.')
