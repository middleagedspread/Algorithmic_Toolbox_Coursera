# Python 3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i
    return -1


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4
    left = 0
    right = len(keys)-1

    while left < right:
        midpoint = (left + right) // 2  # this avoids overflow
        if keys[midpoint] < query:
            left = midpoint+1
        else:
            right = midpoint
    if keys[left] == query:
        return left
    return -1  # not present in array


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
