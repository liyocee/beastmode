

"""
Given n => return 1 + 2 + 3 ... + n-1 + n
"""
def sum_by_loop(n):
    total = 0

    for i in range(1, n + 1):
        total += i
    return total


"""
Given n => return 1 + 2 + 3 ... + n-1 + n
"""
def sum_by_formula(n):
    """
    use Gauss formula:  n(n+1) / 2
    """
    return (n * (n + 1)) // 2


if __name__ == "__main__":
    for n in [0, 1, 4, 10, 100, 12345]:
        assert sum_by_loop(n) == sum_by_formula(n)
    assert sum_by_formula(4) == 10 and sum_by_formula(10) == 55