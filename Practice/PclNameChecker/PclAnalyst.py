import os
from PclNameChecker.PaperType import PaperType
from PclNameChecker.PaperSize import PaperSize
from PclNameChecker.PrintQuality import PrintQuality


PCL_START = b'\x1b\x25\x2d\x31\x32\x33\x34\x35'
PCL_START_LEN = len(PCL_START)

DUPLEX_MODE_START = b'\x1b\x26\x6c'
DUPLEX_MODE_END = 0x53
DUPLEX_MODE_LEN = len(DUPLEX_MODE_START) + 2

MEDIA_SRC_START = DUPLEX_MODE_START
MEDIA_SRC_END = 0x48
MEDIA_SRC_LEN = DUPLEX_MODE_LEN

PRINT_QUALITY_START = b'\x1b\x2a\x6f'
PRINT_QUALITY_END = 0x4d
PRINT_QUALITY_LEN = DUPLEX_MODE_LEN

PAPER_SIZE_START = DUPLEX_MODE_START
PAPER_SIZE_END = 0x41
PAPER_SIZE_LEN = DUPLEX_MODE_LEN

PAPER_TYPE_START = DUPLEX_MODE_START
PAPER_TYPE_END = 0x4d
PAPER_TYPE_LEN = DUPLEX_MODE_LEN

PAPER_BREAK = b'\x1b\x2a\x72\x43'
PAPER_BREAK_LEN = len(PAPER_BREAK)


class PclAnalyst:
    def __init__(self, filename):
        self.__file_name__ = os.path.basename(filename)
        self.__file_path__ = os.path.abspath(filename)[ : str(filename).find(self.__file_name__) - 1]
        self.__pcl_content__, paper_number = self._pcl_title()
        self.__property_map__ = self.analyze()
        self.__property_map__["page_number"] = paper_number

    @property
    def name(self):
        return self.__file_name__

    @property
    def path(self):
        return self.__file_path__

    @property
    def pcl_propertis(self):
        return self.__property_map__

    @property
    def media_source(self):
        return self.__property_map__["media_source"]

    @property
    def paper_type(self):
        return self.__property_map__["paper_type"]

    @property
    def paper_size(self):
        return self.__property_map__["paper_size"]

    @property
    def print_quality(self):
        return self.__property_map__["print_quality"]

    @property
    def duplex_mode(self):
        return self.__property_map__["duplex_mode"]

    @property
    def page_number(self):
        return self.__property_map__["page_number"]

    def _pcl_title(self):
        file = self.__file_path__ + "\\" +  self.__file_name__
        file_handle = open(file, 'rb')
        pcl_content = None
        pcl_page_number = 0
        try:
            read_content = file_handle.read()
            start = read_content.find(PCL_START)
            pos = read_content.find(PAPER_BREAK)
            pcl_page_number = (len(read_content) - start ) // pos + 1
            pcl_content = read_content[start : start + 4 * 1024]
        except:
            raise RuntimeError
        finally:
            file_handle.close()
            return pcl_content, pcl_page_number

    def analyze(self):
        accend = len(DUPLEX_MODE_START)
        #Get pcl media
        property_map = dict()
        # PRINT_QUALITY
        property_map["print_quality"] = self._analyze_pcl("print_quality")
        # PAPER TYPE
        property_map['paper_type'] = self._analyze_pcl('paper_type')
        # Paper size
        property_map['paper_size'] = self._analyze_pcl('paper_size')
        # Duplex mode
        property_map['duplex_mode'] = self._analyze_pcl('duplex_mode')
        # Media source
        property_map['media_source'] = self._analyze_pcl('media_source')
        return property_map
            
    def _analyze_pcl(self, type):
        accent = len(DUPLEX_MODE_START)
        pos = self.__pcl_content__.find(self._get_start(type))
        while pos != -1:
            end1 = self.__pcl_content__[pos + accent + 1]
            end2 = self.__pcl_content__[pos + accent + 2]
            if end1 == self._get_end(type):
                return self._decode(type, self.__pcl_content__[pos + accent] - 48)
            elif end2 == self._get_end(type):
                if self.__pcl_content__[pos + accent] > 48:
                    value = (self.__pcl_content__[pos + accent] - 48) * 10 + \
                            (self.__pcl_content__[pos + accent + 1] - 48)
                else:
                    value = self.__pcl_content__[pos + accent + 1] - 48
                return self._decode(type, value)
            else:
                pos = pos + accent + (self.__pcl_content__[pos + accent : -1]).find(self._get_start(type))

    def _get_start(self, type):
        switch_map = {
            'paper_type'    : PAPER_TYPE_START,
            'paper_size'    : PAPER_SIZE_START,
            'duplex_mode'   : DUPLEX_MODE_START,
            'print_quality' : PRINT_QUALITY_START,
            'media_source'  : MEDIA_SRC_START
        }
        if type in switch_map.keys():
            return switch_map[type]
        else:
            raise ValueError("Invalid value of {}".format(type))
    
    def _get_end(self, type):
        switch_map = {
            'paper_type'    : PAPER_TYPE_END,
            'paper_size'    : PAPER_SIZE_END,
            'duplex_mode'   : DUPLEX_MODE_END,
            'print_quality' : PRINT_QUALITY_END,
            'media_source'  : MEDIA_SRC_END
        }
        if type in switch_map.keys():
            return switch_map[type]
        else:
            raise ValueError("Invalid value of {}".format(type))

    def _decode(self, type, value):
        def decoder(value):
            return value
        switch_map = {
            'paper_type' : PaperType.decode_from_value,
            'paper_size' : PaperSize.decode_from_value,
            'print_quality' : PrintQuality.decode_from_value,
            'duplex_mode' : decoder,
            'media_source' : decoder
        }
        if type in switch_map.keys():
            result = switch_map[type](value)
            return result
        else:
            raise ValueError('Wrong value of argument - {}'.format(type))

if __name__ == '__main__':
    pcl = PclAnalyst('E:\\Projects\\Python\\Practice\\PclNameChecker\\Test.pcl')
    print(pcl.__property_map__)