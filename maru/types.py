from typing import Iterable, Mapping, Sequence, Tuple

Index = int
Indices = Sequence[Index]
Offset = int

Word = str
Text = Sequence[Word]

FeatureName = str
FeatureValue = float
Feature = Tuple[FeatureName, FeatureValue]
FeatureVector = Iterable[Feature]
FeatureWindow = Iterable[Tuple[Offset, FeatureVector]]

StringVocabulary = Mapping[str, Index]
