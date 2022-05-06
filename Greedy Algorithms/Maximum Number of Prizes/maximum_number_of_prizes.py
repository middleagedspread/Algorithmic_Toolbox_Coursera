# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    # The sum of the first k natural numbers is k(k+1)/2
    # We are looking for the largest k for a given n
    # rearranging k(k+1)/2 <= n gives us
    # k <= ((8n +1)**0.5 - 1) / 2
    # find k then a for loop to create the integers
    number_of_prizes = int(((8 * n + 1) ** 0.5 - 1) // 2)  # note floor division

    for i in range(1, int(number_of_prizes)):  # O(n**0.5)
        summands.append(i)
    sum_of_prizes = (number_of_prizes-1) * number_of_prizes / 2
    summands.append(int(n-sum_of_prizes))

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
