import enum


class Grammeme(str, enum.Enum):
    def __init_subclass__(cls):
        enum.unique(cls)
