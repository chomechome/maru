import functools
import json
import os
from typing import Dict

import keras
from sklearn.externals import joblib

from maru.feature.extractor import IFeatureExtractor
from maru.feature.vocabulary import FeatureVocabulary
from maru.tag import Tag

_get_path = functools.partial(os.path.join, os.path.dirname(__file__))


def load_extractor() -> IFeatureExtractor:
    return joblib.load(_get_path('extractor.joblib'))


def load_tags() -> Dict[int, Tag]:
    return joblib.load(_get_path('tags.joblib'))


def load_tagger() -> keras.Model:
    return keras.models.load_model(_get_path('tagger.h5'))


def load_char_vocabulary() -> FeatureVocabulary:
    with open(_get_path('char_vocabulary.json'), encoding='utf8') as f:
        return FeatureVocabulary(json.load(f))


def load_grammeme_vocabulary() -> FeatureVocabulary:
    with open(_get_path('grammeme_vocabulary.json'), encoding='utf8') as f:
        return FeatureVocabulary(json.load(f))
