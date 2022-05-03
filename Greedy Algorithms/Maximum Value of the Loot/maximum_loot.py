# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    if capacity == 0 or not weights:
        return 0

    max_index = prices.index(max(prices))
    # print(f"max_index: {max_index}")
    amount = min(weights[max_index],capacity)
    # print(f"amount: {amount}")
    value = prices[max_index] * amount / weights[max_index]
    # print(f"value: {value}")
    capacity -= amount
    # print(f"new capacity: {capacity}")
    weights.pop(max_index)
    prices.pop(max_index)
    return value + maximum_loot_value(capacity, weights, prices)



if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))

# print (maximum_loot_value(10, [30], [500]))

