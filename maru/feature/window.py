from typing import Iterable, Mapping

from maru.feature.extractor import IFeatureExtractor
from maru.types import Index, Indices, Offset, Text, FeatureWindow


class FeatureWindowGenerator:
    def __init__(self, extractors: Mapping[Offset, IFeatureExtractor]):
        self._extractors = extractors

    def _get_window(self, text: Text, center: Index) -> FeatureWindow:
        length = len(text)
        for offset, extractor in self._extractors.items():
            index = center + offset
            if 0 <= index < length:
                features = extractor.extract(text[index])
                yield (offset, features)

    def generate(self,
                 text: Text,
                 indices: Indices) -> Iterable[FeatureWindow]:
        for center in indices:
            yield self._get_window(text, center)
