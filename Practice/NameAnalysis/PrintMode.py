from enum import Enum


## Enum of print mode, contains draft, normal and best
class PrintMode(Enum):
    Draft = 0
    Normal = 1
    Best = 2
    Unknown = 3

    def __init__(self, value):
        self.__value__ = value

    @property
    def value(self):
        return self.__value__

    def __str__(self):
        str_map = {
            self.Normal : 'Normal',
            self.Draft : 'Draft',
            self.Best : 'Best',
            self.Unknown : 'Unknown'
        }
        return str_map[self]

    @classmethod
    def decode_from_str(cls, print_mode_str):
        print_mode_str = str(print_mode_str)
        if len(print_mode_str) == 1:
            if print_mode_str.upper() in ['D', 'N', 'B']:
                switch_map = {
                    'D' : PrintMode.Draft,
                    'B' : PrintMode.Best,
                    'N' : PrintMode.Normal
                }
                return switch_map[print_mode_str.upper()]
        else:
            if print_mode_str.lower().title() in cls._member_map_.keys():
                return cls._member_map_[print_mode_str.lower().title()]

        return PrintMode.Unknown


if __name__ == '__main__':
    print_mode = PrintMode.decode_from_str("B")
    print(print_mode)