from typing import Iterable

from scipy.sparse import csr_matrix

from maru.feature.vocabulary import PositionalFeatureVocabulary
from maru.types import FeatureWindow


class SparseWindowVectorizer:
    def __init__(self, vocabulary: PositionalFeatureVocabulary):
        self._vocabulary = vocabulary
        self._feature_count = vocabulary.get_feature_count()

    def transform(self, windows: Iterable[FeatureWindow]) -> csr_matrix:
        values = []
        columns = []
        rows = [0]

        vocabulary = self._vocabulary

        for window in windows:
            for position, features in window:
                mapping = vocabulary[position]
                for name, value in features:
                    if name in mapping:
                        columns.append(mapping[name])
                        values.append(value)
            rows.append(len(columns))

        height = len(rows) - 1
        width = self._feature_count

        return csr_matrix(
            (values, columns, rows),
            shape=(height, width),
        )
