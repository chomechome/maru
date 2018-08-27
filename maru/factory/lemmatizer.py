from typing import Iterable

from maru.lemmatizer import (
    ILemmatizer,
    DummyLemmatizer,
    PymorphyLemmatizer,
    Cache,
)


def get_lemmatizer(name: str, cache_size: int) -> ILemmatizer:
    lemmatizers = {
        'dummy': lambda: DummyLemmatizer(),
        'pymorphy': lambda: Cache(PymorphyLemmatizer(), size=cache_size),
    }
    if name not in lemmatizers:
        raise InvalidLemmatizerError(name, lemmatizers)

    return lemmatizers[name]()


class InvalidLemmatizerError(Exception):
    def __init__(self, lemmatizer: str, expected: Iterable[str]):
        super().__init__(f'Invalid lemmatizer {lemmatizer}. '
                         f'Valid lemmatizers are: {", ".join(expected)}.')
