import pymorphy2

from maru.grammeme import PartOfSpeech

_PART_OF_SPEECH = {
    'ADJF': PartOfSpeech.ADJECTIVE,
    'ADJS': PartOfSpeech.ADJECTIVE,
    'ADVB': PartOfSpeech.ADVERB,
    'COMP': PartOfSpeech.ADVERB,
    'CONJ': PartOfSpeech.CONJUNCTION,
    'GRND': PartOfSpeech.VERB,
    'INFN': PartOfSpeech.VERB,
    'INTJ': PartOfSpeech.INTERJECTION,
    'NOUN': PartOfSpeech.NOUN,
    'NPRO': PartOfSpeech.PRONOUN,
    'NUMR': PartOfSpeech.NUMERICAL,
    'NUMB': PartOfSpeech.NUMERICAL,
    'PART': PartOfSpeech.PARTICLE,
    'PNCT': PartOfSpeech.PUNCTUATION,
    'PRCL': PartOfSpeech.PARTICLE,
    'PRED': PartOfSpeech.ADJECTIVE,
    'PREP': PartOfSpeech.ADPOSITION,
    'PRTF': PartOfSpeech.ADJECTIVE,
    'PRTS': PartOfSpeech.ADJECTIVE,
    'VERB': PartOfSpeech.VERB,
}

_DETERMINANTS = {
    'ваш',
    'весь',
    'всякий',
    'всяк',
    'другой',
    'его',
    'её',
    'иной',
    'ихний',
    'их',
    'каждый',
    'каков',
    'какой',
    'какой-либо',
    'какой-нибудь',
    'какой-то',
    'кой',
    'который',
    'который-нибудь',
    'любой',
    'многие',
    'мой',
    'наш',
    'некий',
    'некоторый',
    'немногие',
    'никакой',
    'ничей',
    'оный',
    'прочий',
    'проч.',
    'пр.',
    'свой',
    'сей',
    'таков',
    'такой',
    'твой',
    'тот',
    'чей',
    'чей-либо',
    'чей-нибудь',
    'чей-то',
    'этакий',
    'этот',
}


def get_part_of_speech(parse: pymorphy2.analyzer.Parse) -> PartOfSpeech:
    if parse.word in _DETERMINANTS:
        return PartOfSpeech.DETERMINANT
    return _PART_OF_SPEECH.get(parse.tag.POS, PartOfSpeech.UNKNOWN)
