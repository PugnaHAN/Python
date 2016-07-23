from Tutorial1.ExcelHandler import ExcelHandler
from Tutorial1.AnalyzeFiles import ListFiles


def execute(file_name, dir_path):
    list_files = ListFiles(dir_path,False)
    files =  list_files.files
    excel_handler = ExcelHandler(filename=file_name)
    contents = excel_handler.read()

    for sheet_name in excel_handler.workbook.get_sheet_names():
        sheet_content = contents[sheet_name]
        row = 1
        for dir in files:
            if isinstance(dir, list):
                col = get_col(sheet_content, dir[0])
                if col is not None:
                    for i in range(1, len(dir)):
                        excel_handler.edit(sheet=sheet_name, col=col, row=i + 1,value=dir[i])
        if get_col(sheet_content, 'Other') is not None:
            col = get_col(sheet_content, 'Other')
            for file in files:
                if isinstance(file, str):
                    row += 1
                    excel_handler.edit(sheet=sheet_name, col=col, row=row, value=file)
    excel_handler.close()


def decode_col_from_str(col_str):
    col_str_map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return col_str_map.find(col_str) + 1

def get_col(content, value):
    for key in content:
        if content[key] == value:
            return decode_col_from_str(key[0])
    return None



if __name__ == '__main__':
    file_path = "C:\\Users\\Juhan\\Desktop\\PythonTest"
    file_name = file_path + "\\PythonTest.xlsx"
    execute(file_name, file_path)