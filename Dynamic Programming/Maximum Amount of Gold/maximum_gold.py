# python3

from sys import stdin


def maximum_gold(capacity, weights):  # knapsack problem without repetition, with value = weight for all items
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    # initialise a 2d array of length capacity * len(weights)
    # this will hold the maximum value for each weight (w) up to capacity
    # for individual use of each item
    knapsack_value = [[0 for x in range(capacity+1)] for x in range(len(weights)+1)]
    # for i in knapsack_value:
    #     print(i)
    for item_index in range(1, len(weights)+1):  # run through each item weight in the list
        for weight in range(1, capacity+1):  # run through knapsack weight from 1 to capacity
            knapsack_value[item_index][weight] = knapsack_value[item_index-1][weight]
            # initialise minimum value to the value of this weight of knapsack with one less item
            if weights[item_index-1] <= weight:  # check this item can fit in this size of knapsack
                # find the value of this item added to a knapsack of weight - (w -the weight of this item), with one less item
                value = knapsack_value[item_index-1][weight-weights[item_index-1]] + weights[item_index-1]
                if knapsack_value[item_index][weight] < value:  # if that value is higher than the existing value
                    knapsack_value[item_index][weight] = value  # update the value
    return knapsack_value[len(weights)][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))

# print(maximum_gold(10, (1, 4, 8)))
