# Python 3
import random
import timeit
import bisect


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i
    return -1

# def binary_search(keys, query, left=0, right=None):
#     assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
#     assert 1 <= len(keys) <= 3 * 10 ** 4
#
#     if right is None:
#         right = len(keys)-1
#
#     while right >= left:
#         midpoint = left + (right - left) // 2  # this avoids overflow
#
#         if keys[midpoint] == query:
#             return midpoint
#
#         elif keys[midpoint] > query:
#             right = midpoint-1
#         else:
#             left = midpoint+1
#     return -1  # not present in array

def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
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


# def bisect_binary_search(keys, query):
#     assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
#     assert 1 <= len(keys) <= 3 * 10 ** 4
#
#     index = bisect.bisect_left(keys, query)
#     if index <= len(keys)-1 and keys[index] == query:
#         return index
#     else:
#         return -1



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')



# keys = random.sample(range(1,10**5),10**4)
# keys.sort()
# print("Keys length:", len(keys))
# queries = random.sample(range(1,10**5+1),10**4)
# print("Queries length:", len(queries))
# start = timeit.default_timer()
# answers = []
# for query in queries:
#     answers.append(new_binary_search(keys,query))
# common_indeces = [x for x in answers if x != -1]
# end = timeit.default_timer()
# print(f"runtime: {end - start}")
# print('Number of common indeces:', len(common_indeces))
# start = timeit.default_timer()
# answers = []
# for query in queries:
#     answers.append(bisect_binary_search(keys,query))
# common_indeces = [x for x in answers if x != -1]
# end = timeit.default_timer()
# print(f"runtime: {end - start}")
# print('Number of common indeces:', len(common_indeces))
# start = timeit.default_timer()
# answers = []
# for query in queries:
#     answers.append(binary_search(keys,query))
# common_indeces = [x for x in answers if x != -1]
# end = timeit.default_timer()
# print(f"runtime: {end - start}")
# print('Number of common indeces:', len(common_indeces))


# print(linear_search([1], 3))
# print(new_binary_search([1], 3))
# print(linear_search([3], 3))
# print(new_binary_search([3], 3))
#
# print(new_binary_search([1, 2, 3, 4, 5, 6, 7], 3))
# print(new_binary_search([1, 2, 3, 4, 6, 7, 8, 9], 5))
# print(new_binary_search([1, 2, 3, 4, 5, 6, 7], 7))
# print(new_binary_search([1], 8))
# print(new_binary_search([2,3], 1))
