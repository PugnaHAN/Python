import os


# 创建一个类来记录一个文件夹内的所有文件
# 记录文件的数据结构是list，list的第一个数据表示该文件夹的名称
# 如果遍历到该路径是一个文件，则把文件添加到list中，如果是文件夹则用list来保存其文件夹下的内容
class ListFiles:
    def __init__(self, path = os.getcwd(), delay = True):
        self.__file_path__ = path
        self.__files__ = [os.path.basename(self.__file_path__)]
        if not delay:
            self.list_files()

    @property
    def file_path(self):
        return self.__file_path__

    @file_path.setter
    def file_path(self, path):
        if isinstance(path, str):
            self.__file_path__ = path
        else:
            self.__file_path__ == os.getcwd()

    @property
    def files(self):
        return self.__files__

    def list_files(self, path = None, file_list = None):
        path = path if path is not None else self.__file_path__
        ## path = path.encode('gbk')
        file_list = file_list if file_list is not None else self.__files__
        if len(file_list) > 1:
            return
        files = os.listdir(path)
        for file in files:
            if os.path.isdir(path + '/' + file):
                file_lst = [file]
                file_list.append(file_lst)
                self.list_files(path + '/' + file, file_lst)
            else:
                file_list.append(file)

if __name__ == "__main__":
    # cwd = os.getcwd()
    path = "C:\\Users\\Juhan\\Desktop\\PythonTest"
    list_files = ListFiles(path)
    list_files.list_files(path)
    print(list_files.files)
