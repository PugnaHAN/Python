import optparse
import sys
import os
import struct
from BinaryRecordFile import BinaryRecordFile

def main():
    usage = "Usage: xdump.py [options] file1 [file2 [... fileN]"
    parser = optparse.OptionParser(usage = usage)

    parser.add_option("-b", "--blocksize", type = 'int', 
                      dest = 'blocksize', default = 16,
                      help = 'block size(8...80)[default: 16]')
    parser.add_option("-d", "--decimal", action = "store_false",
                      help = "decimal block numbers [default: hexadecimal]")
    parser.add_option("-e", "--encoding", type = "string",
                      dest = "encoding", default = "utf-8",
                      help = "encoding (ASCII..UTF-32)[default:UTF-8")

    (options, args) = parser.parse_args()
    # print(args)

    print_header()
    print_binary_data(args, options.blocksize, options.encoding, options.decimal)

def print_header():
    HEADER = "{block:<8}  {bytes:<35}  {chars:.^10}" \
                                        .format(block = 'Block',
                                                bytes = 'Bytes',
                                                chars = "UTF-8 characters")
    DIV_LINE = "{0}  {1}  {2}".format('-'*8,
                                      '-'*35,
                                      '-'*16)
    print(HEADER)
    print(DIV_LINE)

def print_binary_data(files, blocksize = 16, encoding = 'utf-8', decimal = False):
    if len(files) == 0:
        return
    for single_file in files:
        # print(single_file)
        brf = BinaryRecordFile(single_file, blocksize - 1)
        for i in range(len(brf)):
            result = format_string(brf[i], blocksize, decimal, encoding)
            # result = None, None
            print("{0}  {1}  {2}".format(i, result[0], result[1]))

def format_string(binary_record, blocksize, decimal, encoding):
    s = "<i{}s".format(blocksize - 5)
    # S = struct.Struct("<i{}s".format(brf[i].record_size - 5))
    data = struct.unpack(s, binary_record)
    print(data[1])
    num_fmt = '0=8d' if decimal == True else "0=8x"
    num_str = "{0:{fmt}} {1:{fmt}} {2:{fmt}} {3:{fmt}}".format(data[1],
                                                               int(data[2]),
                                                               int(data[3]),
                                                               int(data[4]),
                                                               fmt = num_fmt)
    msg_str = "{0:.^10}".format(data[5:].rstrip(b'\x00'))
    print(num_str)
    print(msg_str)
    return num_str, msg_str

main()
