def is_palindrome(nums):
    def is_pal(n):
        num = str(n)
        rev_num = num[-1 : : -1]
        # print(rev_num)
        if num == rev_num:
            return True
        else:
            return False

    return filter(is_pal, nums)

if __name__ == '__main__':
    L = range(1000)
    # print(L)
    print(list(is_palindrome(L)))