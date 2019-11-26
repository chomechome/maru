import functools
import json
import os
from typing import Dict

import numpy
from sklearn.externals import joblib

from maru.feature.extractor import IFeatureExtractor
from maru.feature.vocabulary import PositionalFeatureVocabulary
from maru.tag import Tag

_get_path = functools.partial(os.path.join, os.path.dirname(__file__))


def load_extractor() -> IFeatureExtractor:
    return joblib.load(_get_path('extractor.joblib'))


def load_vocabulary() -> PositionalFeatureVocabulary:
    with open(_get_path('vocabulary.json'), encoding='utf8') as f:
        data = {int(index): mapping for index, mapping in json.load(f).items()}
    return PositionalFeatureVocabulary(data)


def load_tags() -> Dict[int, Tag]:
    return joblib.load(_get_path('tags.joblib'))


def load_coefficients() -> numpy.array:
    return joblib.load(_get_path('coefficients.joblib'))


def load_intercept() -> numpy.array:
    return joblib.load(_get_path('intercept.joblib'))
