import functools
import os
from typing import Dict

import pycrfsuite
from sklearn.externals import joblib

from maru.feature.extractor import IFeatureExtractor
from maru.tag import Tag

_get_path = functools.partial(os.path.join, os.path.dirname(__file__))


def load_extractor() -> IFeatureExtractor:
    return joblib.load(_get_path('extractor.joblib'))


def load_tags() -> Dict[int, Tag]:
    return joblib.load(_get_path('tags.joblib'))


def load_tagger() -> pycrfsuite.Tagger:
    tagger = pycrfsuite.Tagger()
    tagger.open(_get_path('tagger.crfsuite'))
    return tagger
