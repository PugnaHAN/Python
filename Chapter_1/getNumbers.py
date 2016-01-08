def swapNumbers(numbers, index1, index2):
    swappedList = []
    if index1 < index2:
        if index1 > 0 and index2 < (len(numbers) - 1):
            swappedList = numbers[ : index1] +\
                          [numbers[index2]] +\
                          numbers[index1 + 1 : index2] +\
                          [numbers[index1]] +\
                          numbers[index2 + 1:]
        elif index1 == 0:
            swappedList = [numbers[index2]] +\
                          numbers[1: index2] +\
                          [numbers[index1]] +\
                          numbers[index2 + 1:]
        else:
            swappedList = numbers[:index1] +\
                          [numbers[index2]] +\
                          numbers[index1 + 1 : -1] +\
                          [numbers[index1]]
        return swappedList
    else:
        return swapNumbers(numbers, index2, index1)

def sortNumber(numbers):
    i = len(numbers) - 1
    while i > 0:
        j = 0
        while j < i:
            if numbers[j] > numbers[j+1]:
                numbers = swapNumbers(numbers, j, j+1)
            j += 1
        i -= 1
    return numbers

numbers = []

while True:
    try:
        number = input("enter a number of Enter to finish:")
        if not len(number):
            print(numbers)
            print(sortNumber(numbers))
            print("count = " + str(len(numbers)) + \
                  ", sum = " + str(sum(numbers)) + \
                  ", maximum = " + str(max(numbers)) + \
                  ", minimum = " + str(min(numbers)) + \
                  ", mean = " + str(sum(numbers)/len(numbers)))
            break
        else:
           numbers.append(int(number))
    except ValueError as err:
        print(err)

        
