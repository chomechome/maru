import abc

from maru.types import Word, FeatureVector


class IFeatureExtractor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def extract(self, word: Word) -> FeatureVector:
        pass
