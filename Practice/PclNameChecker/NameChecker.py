import os
import time
import optparse
from PclNameChecker.PclAnalyst import PclAnalyst
from PclNameChecker.NameAnalyst import NameDescriptor


def main():
    parser = optparse.OptionParser()
    parser.add_option("-d", "--dir", dest = "directory", type='str',
                      help = ("The path of dirctory which contains all "
                              "files which you want to check [default:%default]"))
    parser.add_option("-f", "--file", dest = "file", type = 'str',
                      help = ("The file which you want to check"))
    parser.add_option("-o", "--output", dest = "output", type = 'str',
                      help = ("The output log file [default:%default]"))
    parser.set_defaults(directory = os.getcwd(), output = str(int(time.time())) + ".log")
    opts, args = parser.parse_args()

    log_file = opts.directory + '\\' + opts.output
    print(log_file)
    log_handler = open(log_file, "w")
    filenames = list()
    try:
        if opts.file is not None:
            filenames.append(opts.file)
        else:
            for f in os.listdir(opts.directory):
                if f.endswith("pcl"):
                    filenames.append(f)
        for filename in filenames:
            filename = opts.directory + "\\" + filename
            pcl_holder = PclAnalyst(filename)
            name_descriptor = NameDescriptor()
            name_descriptor.analysis_from_filename(filename)
            if compare(name_descriptor, pcl_holder):
                log_handler.write(gen_log(filename, name_descriptor, pcl_holder))
    except IOError:
        print("IOEoor happen!")
    finally:
        log_handler.close()

def compare(name_descriptor, pcl_holder):
    if isinstance(name_descriptor, NameDescriptor) and isinstance(pcl_holder, PclAnalyst):
        result =  (name_descriptor.paper_size == pcl_holder.paper_size) and \
                  (name_descriptor.print_quality == pcl_holder.print_quality) and \
                  (name_descriptor.paper_type == pcl_holder.paper_type) and \
                  (name_descriptor.page_number == pcl_holder.paper_number)
        return result
    else:
        raise TypeError("Wrong type of arguments")

def gen_log(filename, name_descriptor, pcl_holder):
    if isinstance(name_descriptor, NameDescriptor) and isinstance(pcl_holder, PclAnalyst):
        msg = """{0}: paper_size  -> name - {1}, pcl - {2};
                    paper_type  -> name - {3}, pcl - {4};
                    print_mode  -> name - {5}, pcl - {6};
                    page_number -> name - {7}, pcl - {8} \n
            """.format(filename, name_descriptor.paper_size, pcl_holder.paper_size,
                       name_descriptor.paper_type, pcl_holder.paper_type,
                       name_descriptor.print_quality, pcl_holder.print_quality,
                       name_descriptor.page_number, pcl_holder.paper_number)
        return msg
    else:
        raise TypeError("Wrong type of arguments")


if __name__ == "__main__":
    main()
