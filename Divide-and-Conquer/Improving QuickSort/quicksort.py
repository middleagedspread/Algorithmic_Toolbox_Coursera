# python3

from random import randint


def partition3(array, left, right):
    pivot_value = array[left]
    i = left
    while i <= right:
        if array[i] < pivot_value:
            array[i], array[left] = array[left], array[i]  # swap values at i and left
            i += 1
            left += 1
        elif array[i] > pivot_value:
            array[i], array[right] = array[right], array[i]  # swap values at i and right
            right -= 1
        elif array[i] == pivot_value:
            i +=1
    return left, right



def randomized_quick_sort(array, left, right):
    if left >= right:  #base case - single element array, do nothing
        return
    k = randint(left, right)  # select a random element
    array[left], array[k] = array[k], array[left]  # swap the first and random element
    # make a call to partition3 and then two recursive calls to randomized_quick_sort
    mid_start, mid_end = partition3(array, left, right)
    randomized_quick_sort(array, left, mid_start-1)
    randomized_quick_sort(array, mid_end+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

# test_array = [6, 4, 8, 3, 6, 8, 9, 2, 6, 3, 2]
# print(test_array)
# # print(str(partition3(test_array,0,len(test_array)-1)))
# randomized_quick_sort(test_array,0,len(test_array)-1)
# print(test_array)

