from maru.analyzer import Analyzer
from maru.factory.lemmatizer import get_lemmatizer
from maru.factory.tagger import get_tagger
from maru.tagger import NumericalTagger, PunctuationTagger


def get_analyzer(
    tagger: str = 'linear', lemmatizer: str = 'pymorphy', cache_size: int = 15000,
):
    return Analyzer(
        taggers=[
            PunctuationTagger(),
            NumericalTagger(),
            get_tagger(name=tagger, cache_size=cache_size),
        ],
        lemmatizer=get_lemmatizer(name=lemmatizer, cache_size=cache_size),
    )
