import string
import sys
import collections

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\""

for filename in sys.argv[1:]:
    # print(open(filename))
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1
                # print(words)
# print(words.values())
for word in sorted(words, key = lambda word : words[word]):
    print("'{0}' occurs {1} times".format(word, words[word]))
