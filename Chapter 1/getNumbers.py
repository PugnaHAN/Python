numbers = []
while True:
    try:
        number = input("enter a number of Enter to finish:")
        if not len(number):
            print(numbers)
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

        
