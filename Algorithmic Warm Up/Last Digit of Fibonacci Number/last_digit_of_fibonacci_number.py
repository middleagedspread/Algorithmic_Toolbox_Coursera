# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    if n > 60:  # the last digit of the fibbonaci sequence repeats after 60 cycles
        n = n % 60
    fibonacci_list = [0, 1]
    for i in range(2, n+1):
        fibonacci_list.append((fibonacci_list[i-1]+fibonacci_list[i-2])%10)
    return fibonacci_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))

# first_sixty = []
# second_sixty = []
# for i in range(1,60):
#     first_sixty.append(last_digit_of_fibonacci_number(i))
#
# for i in range(61,120):
#     second_sixty.append(last_digit_of_fibonacci_number(i))
#
# print(first_sixty)
# print(second_sixty)

