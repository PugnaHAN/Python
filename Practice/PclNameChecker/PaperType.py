from enum import Enum

## Enum of paper size, contains Letter, A4, 4X6 in and 5x7 in
class PaperType(Enum):
    Plain_Paper = 0
    HP_Photo = 5
    HP_Brochure_Glossy = 8
    Special = 2
    HP_Brochure_Matte = 2
    Japanese_Postcard = 2
    Unknown = 20

    def __init__(self, value):
        self.__value__ = value

    @property
    def value(self):
        return self.__value__

    def __str__(self):
        switch = dict()
        for member in self._member_map_.values():
            if member.name.find("_") != -1:
                switch[member.name] = member.name.replace("_", " ")
            else:
                switch[member.name] = member.name

        if self.name in switch.keys():
            return switch[self.name]
        else:
            return 'Unknown'

    @classmethod
    def decode_from_str(cls, paper_type_str):
        switch_case = {
            'HPPhoto'   : PaperType.HP_Photo,
            'HPBrochG'  : PaperType.HP_Brochure_Glossy,
            'HPBrochM'  : PaperType.HP_Brochure_Matte,
            'JPC'        : PaperType.Japanese_Postcard,
            'P'          : PaperType.Plain_Paper,
            'Plain'     : PaperType.Plain_Paper,
            'Special'   : PaperType.Special
        }
        if paper_type_str in switch_case.keys():
            return switch_case[paper_type_str]
        else:
            return PaperType.Unknown

    @classmethod
    def decode_from_value(cls, value):
        for size in cls._member_map_.keys():
            if cls._member_map_[size].value == value:
                return cls._member_map_[size]
        return PaperType.Unknown


if __name__ == '__main__':
    paper_type_str = "Plain"
    paper_type = PaperType.decode_from_str(paper_type_str)
    print(paper_type)