# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(myList):
    number_of_inversions = 0
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        number_of_inversions += compute_inversions(left)
        number_of_inversions += compute_inversions(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:  # if right selected all remaining left inverted
                myList[k] = right[j]
                j += 1
                # add number of remaining left elements to inversion
                number_of_inversions += len(left)-i
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
    return number_of_inversions




if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))


# myList = [54,26,93,17,77,31,44,55,20]
# myList = [6,5,4,3,2,1]
# myList = [3,2,1]
# myList = [4, 1, 4, 1]
# myList2 = myList[:]
#
# count = compute_inversions(myList)
# count2 = compute_inversions_naive(myList2)
#
# print(count)
# print(count2)
