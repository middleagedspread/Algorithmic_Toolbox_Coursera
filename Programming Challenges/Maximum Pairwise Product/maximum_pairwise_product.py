# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(number_list):
    assert len(number_list) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in number_list)
    n = len(number_list)
    if n == 1:
        return number_list[0] * 1
    if n == 2: #if only two elements
        return number_list[0] * number_list[1]

    if number_list[0] > number_list[1]: #assign first two elements to biggest, second biggest
        biggest, second_biggest = number_list[0],  number_list[1]
    else:
        biggest, second_biggest = number_list[1],  number_list[0]

    for i in range(2,n): #compare biggest to remaining eleements
        if number_list[i] >= biggest: # n-2 comparisons
            second_biggest, biggest = biggest, number_list[i]
        elif number_list[i] > second_biggest: # another n-2 comparisons
            second_biggest = number_list[i]
    return biggest * second_biggest


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
