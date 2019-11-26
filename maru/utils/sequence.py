from typing import Optional, Sequence

import numpy


def pad_sequences(
    sequences: Sequence[Sequence[float]],
    max_length: Optional[int] = None,
    value: float = 0.0,
) -> numpy.array:
    count = len(sequences)
    if max_length is None:
        max_length = max(map(len, sequences))

    result = numpy.full(shape=(count, max_length), fill_value=value)
    for index, sequence in enumerate(sequences):
        if sequence:
            sequence = sequence[-max_length:]
            result[index, -len(sequence) :] = sequence

    return result
