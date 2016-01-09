import optparse
import sys
import os
import collections
import datetime, time
# judge the file is hidden or not
# import win32file


File = collections.namedtuple('File', 
                              'name modified size ishidden isdir')

def main():
    usage = "Usage: %prog [options] path"
    parser = optparse.OptionParser(usage = usage)
    # type 类型 
    # action
    parser.add_option("-H", "--hidden", action = "store_false", 
                      help = "show hidden files [default: off]")
    parser.add_option("-m", "--modified", action = "store_false",
                      help = ("show last modified date/time [default: off]"))
    parser.add_option("-o", "--order", type = 'choice', dest = "order", 
                    choices = ['name', 'n', 'modified', 'm', 'size', 's'],
                    default = 'name',
                    help = ("ordder by ('name', 'n', 'modified', " 
                            "'m', 'size', 's') [default: name]"))
    parser.add_option("-s", "--size", action = "store_false", 
                    help = "show sizes [default: off]")

    (opts, args) = parser.parse_args()
    print(opts)
    
    files = list()
    # Main actions of list all files
    current_path = os.path.abspath('.')
    files = get_files(current_path)
    print_result(files, sys.argv)    

def get_files(current_path):
    files = list();
    file_names = os.listdir(current_path)
    for filename in file_names:
        file_size = os.path.getsize(filename)
        file_modified = os.path.getmtime(filename)
        file_isdir = os.path.isdir(filename)
        file_ishidden = ishidden(filename)
        single_file = File(filename + ('/' if file_isdir else ''),
                            file_modified, 
                            file_size, file_ishidden,
                            file_isdir)
        files.append(single_file)
    return files

def ishidden(filename):
    if filename[0] == '.':
        return True
    else:
        return False

class WrongTypeException(Exception):pass
def print_result(files, options):
    # print(options)
    # Order type
    if judge_options('-o', '--order', options = options) != -1:
        idx = judge_options('-o', '--order', options = options)
        order_type = options[idx + 1]
        if not order_type in ['name', 'n', 'size', 's', 'modified', 'm']:
        	raise WrongTypeException("Unsupported order type")
        else:
            files = sorted_with_type(files, order_type)
    # print(files)
    
    # Hidden or not
    if judge_options('-H', '--hidden', options = options) != -1:
        hidden = True
    else:
        hidden = False
   
   # Modified time
    if judge_options('-m', '--modified', options = options) != -1:
        modified = True
    else:
        modified = False
    
    print_result_format(files, hidden, modified)

def judge_options(*choice, options):
    for single_choice in choice:
        if single_choice in options:
            return options.index(single_choice)
    return -1


def sorted_with_type(files, order_type):
    if order_type in ['name', 'n']:
        files = sorted(files, key = lambda f : f.name)
    elif order_type in ['modified', 'm']:
        files = sorted(files, key = lambda f : f.modified)
    else:
        files = sorted(files, key = lambda f : f.size)
    return files

def print_result_format(files, hidden = False, modified = False):
    FORMAT_WITH_MODIFIED = "{date_time:<15}{size:>15}  {file_name}"
    FORMAT_WITHOUT_MODIFIED = "{file_name:<20}{size:>15}{date_time}"
    format_type = FORMAT_WITHOUT_MODIFIED \
        if modified == False else FORMAT_WITH_MODIFIED

    for single_file in files:
        if not hidden:
            if single_file.ishidden == True:
                continue
        date_time = format_time(single_file.modified, modified)
        print(format_type.format(date_time = date_time,
                                 size = single_file.size,
                                 file_name = single_file.name))
    
def format_time(date_time, has_time = False):
    t = time.localtime(date_time)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", t)
    return time_str if has_time == True else ''

main()
