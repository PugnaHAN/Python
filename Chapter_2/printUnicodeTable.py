import sys
import unicodedata

def print_unicode_table(word):
    print("decimal    hex    char    {0:^40}".format("name"))
    print("-------    ---    ----    {0:-<40}".format(""))

    if word is None or word in name.lower():
        code = ord(" ")
        end = sys.maxunicode
        while code < end:
            c = chr(code)
            name = unicodedata.name(c, "***unknown***")
            print("{0:7} {0:6X}    {0:^5c}   {1}".format(code,
                                                         name.title()))
            code += 1
    else:
        for char in word:
            code = ord(char)
            name = unicodedata.name(char, "***unknown***")
            print("{0:7} {0:6X}    {0:^5c}   {1}".format(ord(char),
                                                         name.title()))

word = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0}[string]".format(sys.argv[0]))
        word = 0
    else:
        word = sys.argv[1].lower()

if word != 0:
  print_unicode_table(word)