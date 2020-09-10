import gzip
import json
import pathlib
from typing import Dict

import joblib
import numpy

from maru.feature.extractor import IFeatureExtractor
from maru.feature.vocabulary import PositionalFeatureVocabulary
from maru.tag import Tag

_DIRECTORY = pathlib.Path(__file__).parent.absolute()


def load_extractor() -> IFeatureExtractor:
    return joblib.load(_DIRECTORY / 'extractor.joblib')


def load_vocabulary() -> PositionalFeatureVocabulary:
    with (_DIRECTORY / 'vocabulary.json').open(encoding='utf8') as f:
        data = {int(index): mapping for index, mapping in json.load(f).items()}
    return PositionalFeatureVocabulary(data)


def load_tags() -> Dict[int, Tag]:
    return joblib.load(_DIRECTORY / 'tags.joblib')


def load_coefficients() -> numpy.array:
    with gzip.open(_DIRECTORY / 'coefficients.gz', 'rb') as data:
        return numpy.load(data)


def load_intercept() -> numpy.array:
    with gzip.open(_DIRECTORY / 'intercept.gz', 'rb') as data:
        return numpy.load(data)
