from typing import Iterable

from scipy.sparse import csr_matrix

from maru.feature.vocabulary import FeatureVocabulary
from maru.types import FeatureVector


class SparseFeatureVectorizer:
    def __init__(self, vocabulary: FeatureVocabulary):
        self._vocabulary = vocabulary

    def transform(self, features: Iterable[FeatureVector]) -> csr_matrix:
        values = []
        columns = []
        rows = [0]

        vocabulary = self._vocabulary

        for vector in features:
            for name, value in vector:
                if name in vocabulary:
                    columns.append(vocabulary[name])
                    values.append(value)
            rows.append(len(columns))

        height = len(rows) - 1
        width = len(vocabulary)

        return csr_matrix((values, columns, rows), shape=(height, width))
