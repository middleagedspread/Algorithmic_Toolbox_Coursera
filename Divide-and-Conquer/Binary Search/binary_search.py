# python3
import random
import timeit

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i
    return -1

def recursive_binary_search(keys, query, left=0, right=None):
    # This is much slower than the iterative binary search
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    if right is None:
        right = len(keys)-1

    if right >= left:
        midpoint = left + (right - left) // 2  # this avoids overflow

        if keys[midpoint] == query:
            return midpoint

        elif keys[midpoint] > query:
            return binary_search(keys, query, left, midpoint-1)
        else:
            return binary_search(keys, query, midpoint+1, right)

    else:
        return -1  # not present in array

        # print("low index:", low, "low value:", keys[low])
        # print("mid index:", midpoint, "mid value:", keys[midpoint])
        # print("high index:", high, "high value:", keys[high])


def binary_search(keys, query, left=0, right=None):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    if right is None:
        right = len(keys)-1

    while right >= left:
        midpoint = left + (right - left) // 2  # this avoids overflow

        if keys[midpoint] == query:
            return midpoint

        elif keys[midpoint] > query:
            right = midpoint-1
        else:
            left = midpoint+1
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

# print(linear_search([1], 3))
# print(binary_search([1], 3))
# print(linear_search([3], 3))
# print(binary_search([3], 3))
#
# print(binary_search([1, 2, 3, 4, 5, 6, 7], 3))
# print(binary_search([1, 2, 3, 4, 6, 7, 8, 9], 5))
# print(binary_search([1, 2, 3, 4, 5, 6, 7], 7))
# print(binary_search([1], 8))
# print(binary_search([2,3], 1))


# keys = random.sample(range(1,10**4+1),10**4)
# keys.sort()
# print("Keys length:", len(keys))
# queries = random.sample(range(1,10**4+1),10**3)
# print("Queries length:", len(queries))
# start = timeit.default_timer()
# answers = []
# for query in queries:
#     answers.append(binary_search(keys,query))
# common_indeces = [x for x in answers if x != -1]
# end = timeit.default_timer()
# print(f"runtime: {end - start}")
# print('Number of common indeces:', len(common_indeces))

# print(binary_search(list(range(10 ** 4)), 10 ** 4,))
# print(binary_search(list(range(10 ** 4)), 48))
# print(binary_search(list(range(10 ** 4)), 239))
