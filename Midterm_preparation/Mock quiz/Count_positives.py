def count_positives(lst):
    if not lst:
        return 0
    current = 1 if lst[0] > 0 else 0
    return current + count_positives(lst[1:])
result = count_positives([3, -2, 5])
print(result)
