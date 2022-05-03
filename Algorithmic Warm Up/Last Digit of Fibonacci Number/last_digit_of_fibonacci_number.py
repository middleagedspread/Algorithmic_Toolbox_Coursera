# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


# def last_digit_of_fibonacci_number(n):  # using a list
#     assert 0 <= n <= 10 ** 7
#     if n > 60:  # the last digit of the fibbonaci sequence repeats after 60 cycles
#         n = n % 60
#     fibonacci_list = [0, 1]
#     for i in range(2, n+1):
#         fibonacci_list.append((fibonacci_list[i-1]+fibonacci_list[i-2])%10)
#     return fibonacci_list[n]

def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n > 60:  # the last digit of the fibbonaci sequence repeats after 60 cycles
        n = n % 60
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))

# first_sixty = []
# second_sixty = []
# for i in range(200,250):
#     first_sixty.append(last_digit_of_fibonacci_number(i))
#
# for i in range(200, 250):
#     second_sixty.append(last_digit_of_fibonacci_number_try(i))
#
# print(last_digit_of_fibonacci_number(240))
# print(last_digit_of_fibonacci_number_try(240))

