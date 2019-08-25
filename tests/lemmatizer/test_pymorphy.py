from maru.grammeme import PartOfSpeech
from maru.lemmatizer import PymorphyLemmatizer
from maru.tag import Tag


def test():
    lemmatizer = PymorphyLemmatizer()

    assert 'мыть' == lemmatizer.lemmatize('мыло', Tag(pos=PartOfSpeech.VERB))
