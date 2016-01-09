def is_balanced(text, brackets = "()[]{}<>"):
    counts = {}
    left_or_right = {}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left] = 0
        left_or_right[right] = left
    # print(counts)
    # print(left_or_right)
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_or_right:
            left = left_or_right[c]
            if counts[left] == 0:
                return False
            counts[left] -= 1
    return not any(counts.values())

print(is_balanced("hello()"))
