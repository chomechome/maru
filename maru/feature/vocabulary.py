import collections
from typing import Counter, Dict, Iterable, List

from maru.feature.window import FeatureWindow
from maru.types import FeatureName, FeatureVector, Index, Offset


class FeatureVocabulary(Dict[FeatureName, Index]):
    @classmethod
    def train(cls, features: Iterable[FeatureVector], min_count: int = 2):
        counts: Counter[str] = collections.Counter()
        for vector in features:
            counts.update(name for name, _ in vector)

        names = (name for name, count in counts.items() if count >= min_count)
        vocabulary = {name: index for index, name in enumerate(names)}

        return cls(vocabulary)


class PositionalFeatureVocabulary(Dict[Offset, FeatureVocabulary]):
    @classmethod
    def train(cls, windows: Iterable[FeatureWindow], min_count: int = 2):
        features_by_offset: Dict[Offset, List[FeatureVector]] = collections.defaultdict(
            list
        )
        for window in windows:
            for offset, feature_vector in window:
                features_by_offset[offset].append(feature_vector)

        vocabulary_by_offset: Dict[Offset, FeatureVocabulary] = {}
        for offset, feature_matrix in features_by_offset.items():
            feature_count = (
                max(max(vocab.values()) for vocab in vocabulary_by_offset.values()) + 1
            )

            vocabulary = FeatureVocabulary.train(feature_matrix, min_count)
            for feature in vocabulary.keys():
                vocabulary[feature] += feature_count

            vocabulary_by_offset[offset] = vocabulary

        return cls(vocabulary_by_offset)

    def get_feature_count(self):
        max_index = max(max(vocab.values()) for vocab in self.values())
        return max_index + 1
