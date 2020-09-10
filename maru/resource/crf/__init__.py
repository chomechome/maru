import pathlib
from typing import Dict

import joblib
import pycrfsuite

from maru.feature.extractor import IFeatureExtractor
from maru.tag import Tag

_DIRECTORY = pathlib.Path(__file__).parent.absolute()


def load_extractor() -> IFeatureExtractor:
    return joblib.load(_DIRECTORY / 'extractor.joblib')


def load_tags() -> Dict[int, Tag]:
    return joblib.load(_DIRECTORY / 'tags.joblib')


def load_tagger() -> pycrfsuite.Tagger:
    tagger = pycrfsuite.Tagger()
    tagger.open(str(_DIRECTORY / 'tagger.crfsuite'))
    return tagger
