from typing import NamedTuple, Optional

from maru.grammeme import (
    Animacy,
    Aspect,
    Case,
    Degree,
    Gender,
    Mood,
    Number,
    NumericalForm,
    PartOfSpeech,
    Person,
    Tense,
    Variant,
    VerbForm,
    Voice,
)


class Tag(NamedTuple):
    pos: PartOfSpeech
    animacy: Optional[Animacy] = None
    aspect: Optional[Aspect] = None
    case: Optional[Case] = None
    degree: Optional[Degree] = None
    gender: Optional[Gender] = None
    mood: Optional[Mood] = None
    number: Optional[Number] = None
    numform: Optional[NumericalForm] = None
    person: Optional[Person] = None
    tense: Optional[Tense] = None
    variant: Optional[Variant] = None
    verbform: Optional[VerbForm] = None
    voice: Optional[Voice] = None

    def __repr__(self):
        grammemes = (
            f'{key}={value}'
            for key, value in self._asdict().items()
            if value is not None
        )
        return f'{type(self).__name__}({",".join(grammemes)})'
