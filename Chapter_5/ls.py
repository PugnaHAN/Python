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
    # opts --> Options, like -h, -H, -m
    print(opts)
    # arguments --> at this program, it indicates to the filename
    # print(args)

    files = list()
    # Main actions of list all files
    if len(args) == 0:
        current_path = os.path.abspath('.')
        print_result(files, opts)
    else:
        for arg in args:
            current_path = arg
            files = get_files(current_path)
            print_result(files, opts)    

def get_files(current_path):
    files = list();
    file_names = os.listdir(current_path)
    for filename in file_names:
        if current_path != '.':
            filename = current_path + '/' + filename
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
    details = filename.split('/')
    if details[-1][0] == '.':
        return True
    else:
        return False

class WrongTypeException(Exception):pass
def print_result(files, options):
    # print(options)
    # Order type
    order_type = options.order
    if not order_type in ['name', 'n', 'size', 's', 'modified', 'm']:
    	raise WrongTypeException("Unsupported order type")
    else:
        files = sorted_with_type(files, order_type)
    
    # Hidden or not
    hidden = options.hidden
   
    # Modified time
    modified = options.modified
    
    print_result_format(files, hidden, modified)

def sorted_with_type(files, order_type):
    if order_type in ['name', 'n']:
        files = sorted(files, key = lambda f : f.name)
    elif order_type in ['modified', 'm']:
        files = sorted(files, key = lambda f : f.modified)
    else:
        files = sorted(files, key = lambda f : f.size)
    return files

def print_result_format(files, hidden = False, modified = False):
    HEADER_WITH_MODIFIED = "{date_time:-^15} {size:-^15}  {file_name:-^30}"
    HEADER_WITHOUT_MODIFIED = "{file_name:-^30} {size:-^15}  {date_time}"
    FORMAT_WITH_MODIFIED = "{date_time:<15} {size:>15}  {file_name}"
    FORMAT_WITHOUT_MODIFIED = "{file_name:<30} {size:>15}{date_time}"

    format_type = FORMAT_WITHOUT_MODIFIED \
        if modified == False else FORMAT_WITH_MODIFIED

    header_type = HEADER_WITHOUT_MODIFIED \
        if modified == False else HEADER_WITH_MODIFIED
    print(modified)

    print(header_type.format(date_time = 'Date and Time' \
                                if modified == True else '',
                             size = 'Size',
                             file_name = 'File Name'))

    for single_file in files:
        if not hidden:
            if single_file.ishidden == True:
                continue
        date_time = format_time(single_file.modified, modified)
        size_str = format_size(single_file.size)
        name_str = format_name(single_file.name)
        print(format_type.format(date_time = date_time,
                                 size = size_str,
                                 file_name = name_str))
    
def format_time(date_time, has_time = False):
    t = time.localtime(date_time)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", t)
    return time_str if has_time == True else ''

def format_size(size, high = False):
    if high:
        size = size//1024
    size_str = str(size)
    fmt_str = ''
    remain = len(size_str)%3
    for i in range(len(size_str)//3 + 1):
        if i != len(size_str)//3:
            if remain != 0:
                fmt_str += size_str[3*i : 3*i + remain] + ','
        else:
            fmt_str += size_str[-3:]
    if high:
        fmt_str += ' Kbs'
    else:
        fmt_str += ' bits'
    return fmt_str

def format_name(filename):
    if len(filename) > 30:
        name = '...' + filename[-27:]
    else:
        name = filename
    return name

main()
