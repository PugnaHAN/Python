from enum import Enum

## Enum of paper size, contains Letter, A4, 4X6 in and 5x7 in
class PaperSize(Enum):
    Letter = 1
    A4 = 2
    A = 3
    IIIxV = 4
    IVxVI = 5
    VxVII = 6
    Index_IVxVI = 7
    Index_VxVII = 8
    Index_IIIxV = 9
    B5 = 10
    JPC = 11
    Unknown = 12

    def __init__(self, value):
        self.__value__ = value

    @property
    def value(self):
        return self.__value__

    def __str__(self):
        switch = dict()
        for member in self._member_map_.values():
            if member == PaperSize.IVxVI:
                switch[member.name] = '4x6 in'
            elif member == PaperSize.VxVII:
                switch[member.name] = '5x7 in'
            else:
                switch[member.name] = member.name

        if self.name in switch.keys():
            return switch[self.name]
        else:
            return 'Unknown'

    @classmethod
    def decode_from_str(cls, paper_size_str):
        _roman_number_map_ = {
            '1' : 'I',
            '2' : 'II',
            '3' : 'III',
            '4' : 'IV',
            '5' : 'V',
            '6' : 'VI',
            '7' : 'VII',
            '8' : 'VIII',
            '9' : 'XI',
            '10' : 'X'
        }
        paper_size = str(paper_size_str)
        result = None
        if paper_size.lower().find('x') != -1:
            paper_size = paper_size.lower().replace("_", " ")
            paper_size = paper_size[0] + ' ' + paper_size[2:]
            sizes = paper_size.split()
            if len(sizes) == 2:
                result = "{0}x{1}".format(_roman_number_map_[sizes[0]],
                                          _roman_number_map_[sizes[1]])
            elif len(sizes) == 3:
                result = "{0}_{1}x{2}".format(sizes[2].title(),
                                              _roman_number_map_[sizes[0]],
                                              _roman_number_map_[sizes[1]])
        else:
            result = paper_size_str

        if result is not None:
            if result in cls._member_map_.keys():
                return cls._member_map_[result]

        return PaperSize.Unknown



if __name__ == '__main__':
    paper_size_str = "4x6 Index"
    paper_size = PaperSize.decode_from_str(paper_size_str)
    print(paper_size)