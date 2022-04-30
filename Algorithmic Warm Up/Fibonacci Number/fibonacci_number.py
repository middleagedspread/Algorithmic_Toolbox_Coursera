# python3
fibonacci_dict = {}


def fibonacci_number_naive(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n <= 1:  # base case of 0 or 1
        return n
    if n not in fibonacci_dict:  # if we haven't already computed fibonacci(n), add it to the dictionary
        fibonacci_dict[n] = fibonacci_number(n - 1) + fibonacci_number(n - 2)
    return fibonacci_dict[n]


def fibonacci_number_list(n):
    assert 0 <= n <= 10**6
    fibonacci_list = [0, 1]
    for i in range(2, n+1):
        fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2])
    return fibonacci_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
