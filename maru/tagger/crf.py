from typing import Iterator, Optional

from maru.feature.extractor import Cache
from maru.feature.window import FeatureWindowGenerator
from maru.model import crf
from maru.tagger.abstract import ITagger, Tagged
from maru.types import Indices, Text


class CRFTagger(ITagger):
    def __init__(self, cache_size: Optional[int] = 15000):
        self._tagger = crf.load_tagger()
        self._tags = crf.load_tags()

        extractor = crf.load_extractor()

        if cache_size is not None:
            extractor = Cache(extractor, size=cache_size)

        extractors = {offset: extractor for offset in range(-2, 3)}

        self._generator = FeatureWindowGenerator(extractors)

    def _get_features(self, text: Text):
        for window in self._generator.generate(text, range(len(text))):
            yield {
                f'{position}:{name}': value
                for position, features in window
                for name, value in features
            }

    def tag(self, text: Text, indices: Indices) -> Iterator[Tagged]:
        labels = self._tagger.tag(self._get_features(text))
        for index in indices:
            label = labels[index]
            if label:
                yield index, self._tags[label]
