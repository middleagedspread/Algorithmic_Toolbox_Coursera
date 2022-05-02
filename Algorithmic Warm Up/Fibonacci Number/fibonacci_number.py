# python3

import time
fibonacci_dict = {}

def fibonacci_number_naive(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):  # recursion depth maxes out after about 500 iterations
    assert 0 <= n <= 500
    if n <= 1:  # base case of 0 or 1
        return n
    if n not in fibonacci_dict:  # if we haven't already computed fibonacci(n), add it to the dictionary
        fibonacci_dict[n] = fibonacci_number(n - 1) + fibonacci_number(n - 2)
    return fibonacci_dict[n]


def fibonacci_number_list(n):  # about 10 times faster than the recursive method
    assert 0 <= n <= 10**6
    fibonacci_list = [0, 1]
    for i in range(2, n+1):
        fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2])
    return fibonacci_list[n]

def speed_test():
    start_time = time.time()
    print(fibonacci_number(500))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(fibonacci_number_list(5000))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

# print(fibonacci_number_naive(35))



