from functools import reduce

def str2float(s):
    point = 0
    def fn(x, y):
        nonlocal point
        if y == '.':
            point = 1
            return x
        else:
            if point == 0:
                return 10 * x + y
            else:
                point *= 10
                return x + y/point

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}[s]

    return reduce(fn, map(char2num, s))

if __name__ == '__main__':
    number = '123.456'
    print(str2float(number))