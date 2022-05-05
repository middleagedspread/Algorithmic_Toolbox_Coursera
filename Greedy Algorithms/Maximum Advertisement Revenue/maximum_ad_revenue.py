# python3

from itertools import permutations


def max_dot_product_naive(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def max_dot_product(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    sum_product = 0
    first_sequence.sort(reverse=True)  # O(n log n) - sort both sequences in descending order
    second_sequence.sort(reverse=True)  # O(n log n)
    for i in range(0,len(first_sequence)):  # O(n)
        sum_product += first_sequence[i] * second_sequence[i]  # - calculate the dot product
    return sum_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))

# print(max_dot_product([2, 1], [5, 10]))
# print(max_dot_product([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
# print(max_dot_product([17, 12, 20], [19, 2, 3]))
