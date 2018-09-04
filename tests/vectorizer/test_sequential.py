import numpy

from maru.vectorizer import SequentialVectorizer


def _get_texts():
    return [
        [
            'hello',
            'world',
        ],
        [
            'goodbye',
            'cruel',
            'world',
        ],
        [
            'hello',
            'cruel',
            'mad',
            'world',
        ],
    ]


def _get_vocabulary():
    return {
        'hello': 1,
        'world': 2,
        'cruel': 3,
    }


def _assert_vectorized_equal(vectorizer: SequentialVectorizer,
                             expected: numpy.array,
                             ):
    actual = vectorizer.transform(_get_texts())

    numpy.testing.assert_array_equal(expected, actual)


def test_vocabulary():
    _assert_vectorized_equal(
        vectorizer=SequentialVectorizer(_get_vocabulary()),
        expected=numpy.array(
            [
                [0, 0, 1, 2],
                [0, 0, 3, 2],
                [1, 3, 0, 2],
            ],
        ),
    )


def test_padding():
    _assert_vectorized_equal(
        vectorizer=SequentialVectorizer(_get_vocabulary(), max_length=6),
        expected=numpy.array(
            [
                [0, 0, 0, 0, 1, 2],
                [0, 0, 0, 0, 3, 2],
                [0, 0, 1, 3, 0, 2],
            ],
        ),
    )


def test_truncation():
    _assert_vectorized_equal(
        vectorizer=SequentialVectorizer(_get_vocabulary(), max_length=2),
        expected=numpy.array(
            [
                [1, 2],
                [3, 2],
                [0, 2],
            ],
        ),
    )


def test_missing():
    _assert_vectorized_equal(
        vectorizer=SequentialVectorizer(_get_vocabulary(), missing=-1),
        expected=numpy.array(
            [
                [-1, -1, 1, 2],
                [-1, -1, 3, 2],
                [1, 3, -1, 2],
            ],
        ),
    )
