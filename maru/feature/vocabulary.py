import collections
from typing import Dict, Iterable

from maru.feature.window import FeatureWindow
from maru.types import Index, FeatureName, FeatureVector


class FeatureVocabulary(Dict[FeatureName, Index]):
    @classmethod
    def train(cls, features: Iterable[FeatureVector], min_count: int = 2):
        counts = collections.Counter()
        for vector in features:
            counts.update(name for name, _ in vector)

        names = (name for name, count in counts.items() if count >= min_count)
        vocabulary = {name: index for index, name in enumerate(names)}

        return cls(vocabulary)


class PositionalFeatureVocabulary(Dict[Index, FeatureVocabulary]):
    @classmethod
    def train(cls, windows: Iterable[FeatureWindow], min_count: int = 2):
        vocabularies: Dict[Index, FeatureVocabulary] = {}

        positions = collections.defaultdict(list)
        for window in windows:
            for position, features in window:
                positions[position].append(features)

        offset = 0
        for position, features in positions.items():
            vocabulary = FeatureVocabulary.train(features, min_count)
            for feature in vocabulary.keys():
                vocabulary[feature] += offset

            vocabularies[position] = vocabulary

            offset = max(vocabulary.values()) + 1

        return cls(vocabularies)

    def get_feature_count(self):
        max_index = max(max(vocab.values()) for vocab in self.values())
        return max_index + 1
