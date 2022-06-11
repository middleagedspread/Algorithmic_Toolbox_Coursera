
def partition_problem(values):

    array_sum = sum(values)  # calculate sum of values
    if array_sum % 2 != 0:  # check sum is even
        return 0
    n = len(values)

    # initialise a table  size n+1 x size // 2 + 1
    partition = [[False for i in range(n + 1)] for j in range(array_sum // 2 +1)]
    for i in range(0, n+1):
        partition[0][i] = True

    # fill the partition table in
    # bottom up manner
    for sub_sum in range(1, array_sum // 2 + 1):  # for every sub-sum

        for value_index in range(1, n + 1):  # and for every value
            # check whether this sub-sum can be made with some combination of this value and the preceding values
            # set the intercept to the truth value of the same sub_sum with the previous value (i.e. can the sub_sum be
            # reached already, without the addition of this value)
            partition[sub_sum][value_index] = partition[sub_sum][value_index - 1]
            if sub_sum >= values[value_index - 1]:  # if this value is less than the current sub_sum
                # set it to True if the sub_sum - value was true for the previous value (i.e. can the sub-sum be reached
                # with the addition of this value)
                partition[sub_sum][value_index] = (partition[sub_sum][value_index] or partition[sub_sum - values[value_index - 1]][value_index - 1])

    print(list(values))
    for i in range(len(partition)):
        print(i, ": ", partition[i])

    return 1* partition[array_sum // 2][n]



print(partition_problem((5, 10, 12, 3)))
