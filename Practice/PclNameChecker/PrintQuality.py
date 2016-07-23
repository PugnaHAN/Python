from enum import Enum


## Enum of print mode, contains draft, normal and best
class PrintQuality(Enum):
    Normal = 0
    Best = 1
    Draft = 2
    MaxDpi = 3
    Unknown = 4

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
            self.MaxDpi: 'MaxDpi',
            self.Unknown : 'Unknown'
        }
        return str_map[self]

    @classmethod
    def decode_from_str(cls, print_mode_str):
        print_mode_str = str(print_mode_str)
        if len(print_mode_str) == 1:
            if print_mode_str.upper() in ['D', 'N', 'B', 'M']:
                switch_map = {
                    'D' : PrintQuality.Draft,
                    'B' : PrintQuality.Best,
                    'N' : PrintQuality.Normal,
                    'M' : PrintQuality.MaxDpi
                }
                return switch_map[print_mode_str.upper()]
        else:
            if print_mode_str.lower().title() in cls._member_map_.keys():
                return cls._member_map_[print_mode_str.lower().title()]
        return PrintQuality.Unknown

    @classmethod
    def decode_from_value(cls, value):
        for size in cls._member_map_.keys():
            if cls._member_map_[size].value == value:
                return cls._member_map_[size]
        return PrintQuality.Unknown

if __name__ == '__main__':
    print_mode = PrintQuality.decode_from_str("N")
    print(print_mode)