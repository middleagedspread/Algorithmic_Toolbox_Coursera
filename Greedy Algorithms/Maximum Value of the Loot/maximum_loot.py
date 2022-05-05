# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    length = int(len(weights))
    loot = 0
    value_list = []  # create list to hold weights, prices, and price/weight

    for i in range(0, length):  # O(n)
        value_list.append([prices[i], weights[i], prices[i]/weights[i]])

    # sort the list on the price / weight, ascending
    value_list.sort(key=lambda x: x[2], reverse=True)  # O(n log n)

    i = 0
    while capacity > 0 and i < length:  # O(n)
        amount = min(value_list[i][1], capacity)  # get the next amount
        loot += amount * value_list[i][2]  # increment the loot
        capacity -= amount  # decrement the remaining capacity
        i += 1  # move to the next element of the list

    return loot


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))

# print(maximum_loot_value(50, [20, 50, 30], [60, 100, 120]))
# print (maximum_loot_value(10, [30], [500]))
# print(maximum_loot_value(100, [30, 40, 20], [60, 100, 120]))
