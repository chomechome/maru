from typing import Sequence

from maru.grammeme import PartOfSpeech
from maru.lemmatizer import DummyLemmatizer
from maru.morph import Morph
from maru.analyzer import Analyzer
from maru.tag import Tag
from maru.tagger import ITagger
from maru.types import Text
from tests.stubs.tagger import SingleWordTagger

_UNKNOWN = Tag(pos=PartOfSpeech.UNKNOWN)


def _assert_analyzed_equal(expected: Sequence[Morph],
                           taggers: Sequence[ITagger],
                           text: Text,
                           ):
    analyzer = Analyzer(taggers, lemmatizer=DummyLemmatizer())

    assert expected == list(analyzer.analyze(text))


def test_unknown():
    _assert_analyzed_equal(
        expected=[
            Morph(
                word='hello',
                lemma='hello',
                tag=_UNKNOWN,
            ),
        ],
        taggers=[],
        text=['hello'],
    )


def test_tag():
    tag = Tag(pos=PartOfSpeech.NOUN)

    _assert_analyzed_equal(
        expected=[
            Morph(
                word='hello',
                lemma='hello',
                tag=tag,
            ),
        ],
        taggers=[
            SingleWordTagger(
                word='hello',
                tag=tag,
            ),
        ],
        text=['hello'],
    )


def test_tag_partially():
    tag = Tag(pos=PartOfSpeech.ADJECTIVE)

    _assert_analyzed_equal(
        expected=[
            Morph(
                word='hello',
                lemma='hello',
                tag=_UNKNOWN,
            ),
            Morph(
                word='world',
                lemma='world',
                tag=tag,
            ),
        ],
        taggers=[
            SingleWordTagger(
                word='world',
                tag=tag,
            ),
        ],
        text=['hello', 'world'],
    )
