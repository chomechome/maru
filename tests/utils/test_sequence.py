from typing import Sequence

import numpy
import pytest

from maru.utils.sequence import pad_sequences


@pytest.mark.parametrize(
    ['sequences', 'max_length', 'value', 'expected'],
    [
        # keep shape of empty array
        (
            [[], []],
            None,
            0,
            numpy.array([[], []]),
        ),

        # pad array w.r.t. `max_length`
        (
            [[], []],
            2,
            0,
            numpy.array([[0, 0], [0, 0]]),
        ),
        (
            [[], []],
            2,
            1,
            numpy.array([[1, 1], [1, 1]]),
        ),

        # keep shape of non-empty array
        (
            [[1., 2.], [3., 4., 5.]],
            None,
            0,
            numpy.array([[0., 1., 2.], [3., 4., 5.]]),
        ),
        (
            [[3, 4, 5], [6], [7]],
            None,
            -1,
            numpy.array([[3, 4, 5], [-1, -1, 6], [-1, -1, 7]]),
        ),

        # truncate array w.r.t. `max_length`
        (
            [[1, 2, 3, 4], [5]],
            2,
            0,
            numpy.array([[3, 4], [0, 5]]),
        ),
    ]
)
def test_pad_sequences(sequences: Sequence[Sequence[float]],
                       max_length: int,
                       value: float,
                       expected: numpy.array,
                       ):
    actual = pad_sequences(sequences, max_length, value)

    numpy.testing.assert_array_equal(expected, actual)
