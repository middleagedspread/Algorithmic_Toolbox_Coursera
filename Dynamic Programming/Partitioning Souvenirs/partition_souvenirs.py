from itertools import product
from sys import stdin


def partition3_naive(values):
    for c in product(range(3), repeat=len(values)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(values[k] for k in range(len(values)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

# Function for solving the 3–partition problem.
# It returns true if there exist three subsets with the given sum
def subsetSum(values, index_of_next_integer, subset_sum_a, subset_sum_b, subset_sum_c, lookup):

    # return true if the subset is found
    if subset_sum_a == 0 and subset_sum_b == 0 and subset_sum_c == 0:
        return True

    # base case: no items left
    if index_of_next_integer < 0:
        return False

    # construct a unique key from dynamic elements of the input
    key = (subset_sum_a, subset_sum_b, subset_sum_c, index_of_next_integer)

    # if the sub-problem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:

        # Case 1. The current item becomes part of the first subset
        A = False
        if subset_sum_a - values[index_of_next_integer] >= 0:  # if this integer is less than the remaining subset_sum
            # recursively call the algorithm with the integer index decremented and the subset_sum reduced
            A = subsetSum(values, index_of_next_integer - 1, subset_sum_a - values[index_of_next_integer], subset_sum_b, subset_sum_c, lookup)

        # Case 2. The current item becomes part of the second subset
        B = False
        if not A and (subset_sum_b - values[index_of_next_integer] >= 0):  # only called if A is false and this integer < remaining subset_sum
            B = subsetSum(values, index_of_next_integer - 1, subset_sum_a, subset_sum_b - values[index_of_next_integer], subset_sum_c, lookup)

        # Case 3. The current item becomes part of the third subset
        C = False
        if (not A and not B) and (subset_sum_c - values[index_of_next_integer] >= 0):
            C = subsetSum(values, index_of_next_integer - 1, subset_sum_a, subset_sum_b, subset_sum_c - values[index_of_next_integer], lookup)

        # return true if we get a solution
        lookup[key] = A or B or C

    # return the sub-problem solution from the dictionary
    return lookup[key]

def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    if len(values) < 3:
        return False

    # create a dictionary to store solutions to a sub-problem
    lookup = {}

    # get the sum of all elements in the set
    total = sum(values)

    # return true if the sum is divisible by 3 and the set of `values`
    # can be divided into three subsets with an equal sum
    return 1 * ((total % 3) == 0 and subsetSum(values, len(values) - 1, total//3, total//3, total//3, lookup))


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))

# values = (3, 4, 1, 6, 2, 5)
#
# print(partition3_naive(values))
# print(partition3(values))
