from typing import NamedTuple

from maru.grammeme import (
    Animacy,
    Aspect,
    Case,
    Degree,
    Gender,
    Mood,
    Number,
    NumericalForm,
    Person,
    PartOfSpeech,
    Tense,
    Variant,
    VerbForm,
    Voice,
)


class Tag(NamedTuple):
    pos: PartOfSpeech
    animacy: Animacy = None
    aspect: Aspect = None
    case: Case = None
    degree: Degree = None
    gender: Gender = None
    mood: Mood = None
    number: Number = None
    numform: NumericalForm = None
    person: Person = None
    tense: Tense = None
    variant: Variant = None
    verbform: VerbForm = None
    voice: Voice = None

    def __repr__(self):
        grammemes = (f'{key}={value}' for key, value in self._asdict().items()
                     if value is not None)
        return f'{type(self).__name__}({",".join(grammemes)})'
