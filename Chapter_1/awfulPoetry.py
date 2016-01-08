import random
def getRandomType():
    return random.randint(0, 1)

def getRandomWord(words):
    return random.choice(words)

def outputSentences(numbers):
    Articles = ('the', 'a')
    Subjects = ('cat', 'dog', 'man', 'woman', 'boy', 'girl')
    Verbs = ('jumped', 'ran', 'sang', 'cried')
    Adverbs = ("loudly", "quietly", "well", "badley")
    i = 0
    while i < numbers:
        # get the random type
        sentences = getRandomWord(Articles)
        sentences += (" " + getRandomWord(Subjects))
        sentences += (" " + getRandomWord(Verbs))
        if getRandomType():
            sentences += (" " + getRandomWord(Adverbs))
            
        print(sentences)
        sentences = ""
        i += 1

while True:
    try:
        numOfSentences = input("Enter the number of sentences:")
        if len(numOfSentences):
            sentences = int(numOfSentences)
            if( 0< sentences <= 10):
                outputSentences(sentences)
            else:
                print("Invalid number, try again!")
        else:
            break
    except ValueError as err:
        print(err)
