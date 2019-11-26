from typing import Iterator, Optional

import numpy

from maru.feature.extractor import Cache
from maru.resource import rnn
from maru.tagger.abstract import ITagger, Tagged
from maru.types import Indices, Text
from maru.utils.word import normalize
from maru.vectorizer import SparseFeatureVectorizer
from maru.vectorizer.sequential import SequentialVectorizer

_CHAR_INPUT = 'chars'
_GRAMMEME_INPUT = 'grammemes'


class RNNTagger(ITagger):
    def __init__(self, cache_size: Optional[int] = 15000):
        self._tagger = rnn.load_tagger()
        self._tags = rnn.load_tags()

        _, _, max_word_length = self._tagger.get_layer(_CHAR_INPUT).input_shape

        grammeme_vocabulary = rnn.load_grammeme_vocabulary()
        char_vocabulary = rnn.load_char_vocabulary()
        extractor = rnn.load_extractor()

        if cache_size is not None:
            extractor = Cache(extractor, size=cache_size)

        self._extractor = extractor
        self._char_vectorizer = SequentialVectorizer(
            vocabulary=char_vocabulary, max_length=max_word_length,
        )
        self._grammeme_vectorizer = SparseFeatureVectorizer(
            vocabulary=grammeme_vocabulary,
        )

    def _get_network_input(self, text: Text):
        text = [normalize(word) for word in text]

        chars = self._char_vectorizer.transform(sequences=text)
        grammeme_features = map(self._extractor.extract, text)
        grammemes = self._grammeme_vectorizer.transform(grammeme_features)

        return {
            _CHAR_INPUT: numpy.expand_dims(chars, axis=0),
            _GRAMMEME_INPUT: numpy.expand_dims(grammemes.todense(), axis=0),
        }

    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        network_input = self._get_network_input(text)
        labels = self._tagger.predict(network_input)[0].argmax(axis=1)
        for index in indices:
            label = labels[index]
            if label:
                yield index, self._tags[label]
