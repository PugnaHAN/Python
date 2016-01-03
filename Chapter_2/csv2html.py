import sys
import xml.sax.saxutils

def main():
    maxwidth = 1000
    count = 0
    text_file = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')
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
                    print_line(line, color, maxwidth, output_file)
                    count += 1
            except EOFError:
                break        
        print_end(output_file)
    finally:
        text_file.close()
        output_file.close()

def print_start(output_file):
    output_file.write("<table border='1'>\n")

def print_end(output_file):
    output_file.write("</table>\n")   

def print_line(line, color, maxwidth, output_file):
    output_file.write("<tr bgcolor='{0}'>\n".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            output_file.write("<td></td>\n")
        else:
            number = field.replace(",","")
            try:
                x = float(number)
                output_file.write("<td align='right'>{0:d}</td>\n".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace("And ", "and ")
                if len(field) <= maxwidth:
                    field = escape_html(field)
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
    text = text.replace("&", "&amp;")
    text = text.replace("<","&|t;")
    text = text.replace(">", "&gt;")
    return text

main()

