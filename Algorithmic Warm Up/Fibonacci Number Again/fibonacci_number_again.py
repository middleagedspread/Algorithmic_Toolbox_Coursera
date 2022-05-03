# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def pisano_period(m): # for any integer m≥2, the sequence Fn mod m is periodic
    previous, current = 0, 1
    for i in range(0, m * m): # pisano period bound by 0 and m * m
        previous, current = current, (previous + current) % m # calculate the fibonacci sequence
        # as soon as the sequence returns to ...,0,1,... it will repeat
        # A Pisano Period starts with 0,1
        if (previous == 0 and current == 1):
            return i + 1

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    pisano_number = pisano_period(m)

    if n > pisano_number:  # the last digit of the fibbonaci sequence repeats after 60 cycles
        n = n % pisano_number

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    return current


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))

# print(fibonacci_number_again_naive(115,10))
# print(fibonacci_number_again(10,2))

