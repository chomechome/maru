from typing import Iterator, Optional

from maru.feature.extractor import Cache
from maru.feature.window import FeatureWindowGenerator
from maru.model import linear
from maru.tagger.abstract import ITagger, Tagged
from maru.types import Text, Indices
from maru.utils.word import normalize, is_cyrillic
from maru.vectorizer import SparseWindowVectorizer


class LinearTagger(ITagger):
    def __init__(self, cache_size: Optional[int] = 15000):
        self._coefficients = linear.load_coefficients()
        self._intercept = linear.load_intercept()
        self._tags = linear.load_tags()

        vocabulary = linear.load_vocabulary()
        extractor = linear.load_extractor()

        if cache_size is not None:
            extractor = Cache(extractor, size=cache_size)

        extractors = {offset: extractor for offset in vocabulary.keys()}

        self._generator = FeatureWindowGenerator(extractors)
        self._vectorizer = SparseWindowVectorizer(vocabulary)

    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        text = [normalize(word) for word in text]
        indices = [index for index in indices if is_cyrillic(text[index])]

        windows = self._generator.generate(text, indices)
        matrix = self._vectorizer.transform(windows)
        labels = (matrix * self._coefficients + self._intercept).argmax(axis=1)

        for index, label in zip(indices, labels):
            yield index, self._tags[label]
