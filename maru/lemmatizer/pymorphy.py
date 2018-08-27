from maru import pymorphy
from maru.lemmatizer.abstract import ILemmatizer
from maru.tag import Tag
from maru.types import Word


class PymorphyLemmatizer(ILemmatizer):
    def lemmatize(self, word: Word, tag: Tag) -> Word:
        best_parse = max(
            pymorphy.analyze(word),
            key=lambda parse: (
                tag.pos is pymorphy.get_part_of_speech(parse),
                tag.case is pymorphy.get_case(parse),
                tag.gender is pymorphy.get_gender(parse),
            ),
        )
        return best_parse.normal_form
