import abc

from maru.types import FeatureVector, Word


class IFeatureExtractor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def extract(self, word: Word) -> FeatureVector:
        pass
