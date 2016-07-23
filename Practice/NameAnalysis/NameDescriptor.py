from NameAnalysis.PaperSize import PaperSize
from NameAnalysis.PrintMode import PrintMode

class NameDescriptor:
    def  __init__(self, src_name = 'Unknown',
                  paper_size = 'A4',
                  paper_type = 'Plain Paper',
                  print_mode = 'Normal',
                  full_bleed = False,
                  page_number = 1):
        self.__src_name__ = src_name
        self.__paper_size__ = paper_size
        self.__paper_type__ = paper_type
        self.__print_mode__ = print_mode
        self.__full_bleed__ = full_bleed
        self.__page_number__ = page_number

    def __repr__(self):
        if self.__full_bleed__ != False:
            string = "{0}_{1}_{2}_{3}_{4}".format(self.__src_name__ ,
                                                  self.__paper_size__,
                                                  self.__paper_type__,
                                                  self.__print_mode__,
                                                  "FB")
        else:
            string = "{0}_{1}_{2}_{3}".format(self.__src_name__,
                                              self.__paper_size__,
                                              self.__paper_type__,
                                              self.__print_mode__)
        if self.__page_number__ > 1:
            string = string + "_" + str(self.__page_number__) + "pgs"
        return string

    @property
    def src_name(self):
        return self.__src_name__

    @src_name.setter
    def src_name(self, src_name):
        self.__src_name__ = src_name

    @property
    def paper_size(self):
        return self.__paper_size__

    @paper_size.setter
    def paper_size(self, paper_size):
        self.__paper_size__ = paper_size

    @property
    def paper_type(self):
        return self.__paper_type__

    @paper_type.setter
    def paper_type(self, paper_type):
        self.__paper_type__ = paper_type

    @property
    def print_mode(self):
        return self.__print_mode__

    @print_mode.setter
    def print_mode(self, print_mode):
        self.__print_mode__ = print_mode

    @property
    def full_bleed(self):
        return self.__full_bleed__

    @full_bleed.setter
    def full_bleed(self, full_bleed):
        self.__full_bleed__ = full_bleed

    @property
    def page_number(self):
        return self.__page_number__

    @page_number.setter
    def page_number(self, page_number):
        self.__page_number__ = page_number

    def analysis_from_filename(self, filename):
        if isinstance(filename, str):
            file_descriptor = self._smart_analysis(filename)
            self.src_name = file_descriptor[0]
            self.paper_size = PaperSize.decode_from_str(str(file_descriptor[1]).
                                                        replace("_", " ").strip())
            self.paper_type = file_descriptor[2]
            self.print_mode = PrintMode.decode_from_str(file_descriptor[3])
            self.full_bleed = file_descriptor[4]
            self.page_number = file_descriptor[5]
        else:
            raise TypeError("Invalid file name of {}".format(filename))

    def check_validation(self, filename):
        if isinstance(filename, str):
            if not filename.endswith('pcl'):
                return False
        else:
            return False

    def _smart_analysis(self, filename):
        ## Check if there is valid paper size
        filename = str(filename)
        paper_size = "Unknown"
        supported_paper_size = ['_A4_', '_A_', '_Index_', '_B5_', '_4x6_', '_5x7_', '_3x5_', 'JPC']
        for size in supported_paper_size:
            if(filename.find(size) != -1):
                idx = filename.find(size)
                length = len(size)
                if size == '_Index_':
                    idx = idx - 4
                    length = length + 4
                paper_size = filename[idx : idx + length]
                break

        # Check the filename
        filename = self._seperate_filename(filename)
        file_name = ""
        name_lst = filename.split("_")
        if paper_size != 'Unknown':
            for idx in range(len(name_lst)):
                if paper_size.find(name_lst[idx]) != -1:
                    for i in range(idx):
                        file_name = file_name + name_lst[i] + " "
                    break
                else:
                    continue
        else:
            file_name = name_lst[0]
        file_name = file_name.strip()
        # Check the print mode
        idx_of_type = 0
        if paper_size != 'Unknown':
            for idx in range(len(name_lst)):
                if paper_size.find(name_lst[idx]) != -1:
                    idx_of_type = idx + 1
        print_mode = 'Unknown'
        if idx_of_type != 0:
            paper_type = name_lst[idx_of_type]
            if len(paper_type) == 1 and paper_type != 'P':
                paper_type = 'Unknown'
                print_mode = name_lst[idx_of_type]
            else:
                print_mode = name_lst[idx_of_type + 1] if idx_of_type < len(name_lst) - 1 else 'Unknown'
        else:
            for idx in range(len(name_lst)):
                print_mode = PrintMode.decode_from_str(name_lst[idx])
                if print_mode != PrintMode.Unknown:
                    print_mode = print_mode.name
                    paper_type = name_lst[idx - 1]
                    break
                else:
                    paper_type = "Unknown"

        full_bleed = False
        for name in name_lst:
            if name.find('fb') != -1:
                full_bleed = True

        page_number = 1
        if name_lst[-1].find('pgs') != -1:
            page_number = int(name_lst[-1][0])

        return [file_name, (paper_size.replace("_", " ") if paper_size is not None else 'Unknown'),
                paper_type, print_mode, full_bleed, page_number]

    def _seperate_filename(self, filename):
        filename = str(filename)
        name_lst = filename.split("__")
        for name in name_lst:
            if name.find("_") != -1:
                result = name.split("_")
                if len(result) >= 4:
                    return name
            else:
                continue

if __name__ == '__main__':
    filename = 'copperheadXLP__official__PrintFiles__SammySosa_A10env_N_N911a__current.pcl'
    name_descriptor = NameDescriptor()
    name_descriptor.analysis_from_filename(filename)
    print(name_descriptor)