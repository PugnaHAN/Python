import optparse

def main():
    parser = optparse.OptionParser()
    parser.add_option("-w", "--maxwidth", dest = "max_width", type = "int",
                      help = ("""the maximum number of characters that can be
output to string fields [default:%default]"""))
    
    parser.add_option("-f", "--format", dest="format",
                      help = ("""the format used or ouputing numbers
[default: %default]"""))
    parser.set_defaults(max_width = 100, format = ".0f")
    opts, args = parser.parse_args()
    print(opts)
    print(args)

main()
