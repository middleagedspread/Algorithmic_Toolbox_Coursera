# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i
    return -1


def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    if len(keys) == 1:
        if query == keys[0]:
            return 0
        else:
            return -1
    low = 0
    high = len(keys)-1
    # if high < low:
    #     return low-1
    mid = low + (high-low)//2  # get the midpoint (rounded down)

    if query == keys[mid]:
        return mid
    elif query < keys[mid] and keys[0:mid] != []:
        return binary_search(keys[0:mid], query)
    elif keys[mid+1:] != []:
        check_high = binary_search(keys[mid+1:], query)
        if check_high == -1:
            return check_high
        else:
            return check_high  + mid + 1
    else:
        return 0


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

# # print(linear_search([1], 3))
# # print(binary_search([1], 3))
# # print(linear_search([3], 3))
# # print(binary_search([3], 3))
#
# # print(linear_search([1, 2, 3, 4, 5, 6, 7], 3))
# print(binary_search([1, 2, 3, 4, 6, 7, 8, 9], 5))
# print(binary_search([1, 2, 3, 4, 5, 6, 7], 7))
# print(binary_search([1], 8))
# print(binary_search([2,3], 1))

