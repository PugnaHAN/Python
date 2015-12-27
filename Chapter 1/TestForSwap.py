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
            swappedList = numbers[:index] +\
                          [numbers[index2]] +\
                          numbers[index1 + 1 : -1] +\
                          [numbers[index1]]
        return swappedList
    else:
        return swapNumbers(numbers, index2, index1)

numbers = [1, 2, 4, 5, 3, 8, 9]
numbers = swapNumbers(numbers, 4, 2)
print(numbers)
