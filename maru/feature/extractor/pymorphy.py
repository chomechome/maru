from typing import Set

from maru import pymorphy
from maru.feature.extractor.abstract import IFeatureExtractor
from maru.types import Word, FeatureVector


class PymorphyExtractor(IFeatureExtractor):
    def __init__(self, hypotheses: int = 3):
        self._hypotheses = hypotheses

    def extract(self, word: Word) -> FeatureVector:
        seen: Set[str] = set()

        parses = pymorphy.analyze(word)[:self._hypotheses]
        for index, parse in enumerate(parses):
            new = [gram for gram in parse.tag.grammemes if gram not in seen]
            if new:
                yield (f'pymorphy:{index}:score', parse.score)
                for gram in new:
                    yield (f'pymorphy:{index}:{gram}', 1)
                    seen.add(gram)
