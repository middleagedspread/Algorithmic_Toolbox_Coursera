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


def partition3(values, k=3):
    values = list(values)
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    total_sum = sum(values)
    if total_sum % k != 0:  # if the sum is not divisible by k return False
        return False * 1
    target = total_sum // k
    used = [False]*len(values)  # initialise list to flag whether integer has been used

    # sort the array in descending order
    # if the first value is greater than target we cannot partition
    # the array into equal sum subsets == target
    values.sort(reverse=True)
    if values[0] > target:
        return False * 1

    # to reduce the number of recursive calls we will memoise
    # used
    dp = {}

    def backtrack(index, remaining_partitions, subset_sum):
        # since sub-problem depends on used indices of array
        # if same sub-problem occurs again just return dp value
        # print("tuple(used):",tuple(used))
        # for i in dp:
        #     print("dp:",i)
        if tuple(used) in dp:
            return dp[tuple(used)]
        if remaining_partitions == 0:
            return True
        if subset_sum == 0:
            partition = backtrack(0, remaining_partitions-1, target)
            dp[(tuple(used), subset_sum)] = partition
            return partition
        for j in range(index, len(values)):
            if not used[j] and subset_sum-values[j] >= 0:
                used[j] = True
                if backtrack(j+1, remaining_partitions, subset_sum-values[j]):
                    return True
                used[j] = False
        dp[tuple(used)] = False
        return False

    return 1 * backtrack(0, k, target)


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))

# nums = (3, 4, 1, 6, 2, 5)
#
# print(partition3_naive(nums))
# print(partition3(nums))
