# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    if money == 2:
        return 2
    else:
        return int(money/4) + (money % 4 > 0)


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
