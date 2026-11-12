


def find_max(numbers):
    assert len(numbers) > 0
    max = numbers[0]
    comparisons = 0

    for x in numbers[1:]:
        comparisons += 1
        if x > max:
            max = x

    return max, comparisons



if __name__ == "__main__":
    best, count = find_max([4, 17, 9, 2, 17, 30, 1])
    assert best == 30
    assert count == 6

    assert find_max([-5, -1, -8])[0] == -1   # works for negative numbers too
    assert find_max([42]) == (42, 0)         # a one-item list needs no comparisons
