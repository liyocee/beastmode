

"""
Find target in items
return True/False, comparisons count
"""
def linear_search(items, target):
    assert len(items) > 0
    comparisons = 0

    for item in items:
        comparisons += 1
        if item == target:
            return True, comparisons

    return False, comparisons


def binary_search(items, target):
    assert len(items) > 0

    comparisons = 0
    lo = 0
    hi = len(items) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        item = items[mid]
        comparisons += 1

        if item == target:
            return True, comparisons
        if target < item:
            hi = mid - 1
        else:
            lo = mid + 1 

    return False, comparisons


if __name__ == "__main__":
    evens = list(range(0, 2_000_000, 2))    # 0, 2, 4, ..., 1,999,998: one million numbers
    assert len(evens) == 1_000_000 and evens[-1] == 1_999_998

    found, lin = linear_search(evens, 1_234_568)
    assert found and lin == 617_285         # positions 0..617,284 were checked

    found, lin_miss = linear_search(evens, 7)   # 7 is odd, so it is absent
    assert not found and lin_miss == 1_000_000


    found, bin_count = binary_search(evens, 1_234_568)
    assert found and bin_count <= 20

    found, bin_miss = binary_search(evens, 7)
    assert not found and bin_miss <= 20
    
    print("linear:", lin, "binary:", bin_count, "binary on a miss:", bin_miss)