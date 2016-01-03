import sys
import xml.sax.saxutils

file_index = 1

def main():
    print(sys.argv[1])
    if len(sys.argv) < 3 or sys.argv[1] in {"-h", "--help"}:
        print("usage:\ncsv2html.py [maxwidth=int] [format=str] <infile.csv> outfile.html\n")
        print("""maxwidth is an optional integer; if specified, it sets the maximum
number of characters that can be output for string fields,
otherwise a default of 100 characters is used.\n""")
        print("format is the format to use for numbers; if not specified it\n\
defaults to \".Of\".")
    else:
        maxwidth = get_maxwidth()
        fmt = get_format()
        count = 0
        text_file = open(sys.argv[file_index], 'r')
        output_file = open(sys.argv[file_index + 1], 'w')
        print_start(output_file)
        try:
            lines = text_file.readlines()
            while count < len(lines):
                try:                
                    for line in lines:
                        # print(line)
                        if count == 0:
                            color = 'lightgreen'
                        elif count%2:
                            color = 'white'
                        else:
                            color = 'lightyellow'
                        print_line(line, color, maxwidth, fmt, output_file)
                        count += 1
                except EOFError:
                    break        
            print_end(output_file)
        finally:
            text_file.close()
            output_file.close()

def get_maxwidth():
    index_of_maxwidth = -1;
    for i in (1, 2):
        if sys.argv[i].find('maxwidth') != -1:
            index_of_maxwidth = i
            break
    if index_of_maxwidth == -1:
        return 1000
    else:
        global file_index
        file_index += 1
        width = sys.argv[index_of_maxwidth].split("=")
        return int(width[1])

def get_format():
    index_of_format = -1;
    for i in (1, 2):
        if sys.argv[i].find('format') != -1:
            index_of_format = i
            break
    if index_of_format == -1:
        return None
    else:
        global file_index
        file_index += 1
        fmt = sys.argv[index_of_format].split("=")
        return fmt[1]

def print_start(output_file):
    output_file.write("<table border='1'>\n")

def print_end(output_file):
    output_file.write("</table>\n")   

def print_line(line, color, maxwidth, fmt, output_file):
    output_file.write("<tr bgcolor='{0}'>\n".format(color))
    fmt = fmt if fmt is not None else "d"
    # print(fmt)
    fields = extract_fields(line)
    for field in fields:
        if not field:
            output_file.write("<td></td>\n")
        else:
            number = field.replace(",","")
            try:
                x = float(number)
                output_file.write("<td align='right'>{0:fmt}</td>\n".format(x))
            except ValueError:
                field = field.title()
                field = field.replace("And ", "and ")
                if len(field) <= maxwidth:
                    field = escape_html(field)
                    # print(field)
                else:
                    field = "{0}...".format(escape_html(field[:maxwidth]))
                output_file.write("<td>{0}</td>\n".format(field))
    output_file.write("</tr>\n")

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
            continue
        if quote is None and c == ",":
            fields.append(field)
            field =""
        else:
            field += c
    if field:
        fields.append(field)
    return fields

def escape_html(text):
    xml.sax.saxutils.escape(text)
    return text

main()
