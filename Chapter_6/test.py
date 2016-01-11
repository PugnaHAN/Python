def multiple(a,b):
    """
    return a number of a*b
    >>> multiple(5, 4)
    20
    """
    return a*b

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
