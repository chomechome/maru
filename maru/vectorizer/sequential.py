from typing import Iterable

import numpy

from maru.types import Index, StringVocabulary
from maru.utils.sequence import pad_sequences


class SequentialVectorizer:
    def __init__(
        self, vocabulary: StringVocabulary, missing: Index = 0, max_length: int = None,
    ):
        self._vocabulary = vocabulary
        self._missing = missing
        self._max_length = max_length

    def transform(self, sequences: Iterable[Iterable[str]]) -> numpy.array:
        missing = self._missing

        return pad_sequences(
            [
                [self._vocabulary.get(name, missing) for name in sequence]
                for sequence in sequences
            ],
            max_length=self._max_length,
            value=missing,
        )
