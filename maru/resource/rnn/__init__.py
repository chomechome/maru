import json
import pathlib
import typing
from typing import Dict

import joblib

from maru.feature.extractor import IFeatureExtractor
from maru.feature.vocabulary import FeatureVocabulary
from maru.tag import Tag

if typing.TYPE_CHECKING:
    import tensorflow.keras

_DIRECTORY = pathlib.Path(__file__).parent.absolute()


def load_extractor() -> IFeatureExtractor:
    return joblib.load(_DIRECTORY / 'extractor.joblib')


def load_tags() -> Dict[int, Tag]:
    return joblib.load(_DIRECTORY / 'tags.joblib')


def load_tagger() -> 'tensorflow.keras.Model':
    try:
        import tensorflow.keras
    except ModuleNotFoundError:
        raise ImportError(
            'RNN tagger requires TensorFlow. You can install it with "pip install maru[tf]"'
        )
    # this restrains tensorflow from allocating all of available GPU memory
    config = tensorflow.compat.v1.ConfigProto()
    config.gpu_options.allow_growth = True

    tensorflow.compat.v1.keras.backend.set_session(
        tensorflow.compat.v1.Session(config=config)
    )

    return tensorflow.keras.models.load_model(_DIRECTORY / 'tagger.h5')


def load_char_vocabulary() -> FeatureVocabulary:
    with (_DIRECTORY / 'char_vocabulary.json').open(encoding='utf8') as f:
        return FeatureVocabulary(json.load(f))


def load_grammeme_vocabulary() -> FeatureVocabulary:
    with (_DIRECTORY / 'grammeme_vocabulary.json').open(encoding='utf8') as f:
        return FeatureVocabulary(json.load(f))
