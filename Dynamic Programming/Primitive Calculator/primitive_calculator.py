# python3

def map_operators(a):  # this function maps the operator integers to a string of the operation
    if a == 1:
        return "+1"
    elif a == 2:
        return "*2"
    elif a == 3:
        return "*3"
    else:
        return a

def compute_operations(target):
    assert 1 <= target <= 10 ** 6
    available_operators = [1, 2, 3]
    number_of_available_operations = 3

    INF = float('inf')
    # initialise an array to hold minimum number of operations needed to reach target integer
    min_operations_needed = [INF]*(target+1)
    min_operations_needed[0] = 0
    # initialise an array to hold the last operation used for each integer
    last_operation_needed = [0]*(target+1)

    # iterate from 1 to target
    for j in range(1, target+1):
        # for each integer up to target, find the minimum number of operations needed
        # and the last operation used to reach that integer
        minimum = INF
        operator = 0

        for i in range(0, number_of_available_operations):
            # check each operation in available operations
            if available_operators[i] == 1:
                # if the operation is 'add-one'
                if 1+min_operations_needed[j-1] < minimum:
                    minimum = min(minimum, 1+min_operations_needed[j-1])
                    operator = 1
            elif j >= available_operators[i]:
                # if the operator is larger than the target
                # check to see whether using one of these multiplier operators
                # will minimise the operations used to get target
                if j % available_operators[i] == 0:  # if the index j is a multiple of the operator
                    if 1+min_operations_needed[int(j / available_operators[i])] < minimum:  # and if index[j / multiple] +1 < minimum
                        # i.e. add this operator to the number of operations used to reach (target - operation)
                        minimum = 1+min_operations_needed[int(j / available_operators[i])]
                        operator = available_operators[i]
        min_operations_needed[j] = minimum
        last_operation_needed[j] = operator

    # now we have two arrays of length target+1
    # min_operations_needed[] holds the minimum number of operations needed to reach the index of that entry
    # last_operation_needed[] holds the last operation needed to change an amount equal to the index of that entry

    # to get the actual operations used, iterate backwards through the last_operation_needed array
    # starting at target, and reducing the index by the operation used at each step, thus
    # reducing the problem to a solvable sub-problem at each step:
    # F(amount) = F(inverse(operation(amount))) + 1

    amount = target
    operations_used = []
    indeces_used = []

    while amount > 0:
        operations_used.insert(0, last_operation_needed[amount])
        indeces_used.insert(0, amount)
        if last_operation_needed[amount] == 1:
            amount -= 1
        elif last_operation_needed[amount] == 2:
            amount = int(amount/2)
        elif last_operation_needed[amount] == 3:
            amount = int(amount/3)

    # mapped_operations = map(map_operators, operations_used)
    # brackets = "(" * len(operations_used)
    # create a string with the correct formatting for output
    # operations_string = f"{target} = {brackets}0" + ")".join(list(mapped_operations)) + ")"

    # print(min_operations_needed[target]-1)
    # # print(operations_string)
    # print(" ".join(map(str, indeces_used)))
    return indeces_used


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

# input_n = 12
# sequence = compute_operations(input_n)
# print(len(sequence) - 1)
# print(*sequence)
#
# for i in range(len(sequence) - 1):
#     if sequence[i + 1] == sequence[i] + 1:
#         print(sequence[i], "+ 1 = ", sequence[i + 1])
#     elif sequence[i + 1] == 2 * sequence[i]:
#         print(sequence[i], "* 2 = ", sequence[i + 1])
#     else:
#         print(sequence[i], "* 3 = ", sequence[i+1])
