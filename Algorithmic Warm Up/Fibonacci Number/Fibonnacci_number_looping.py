# python3
# fibbo_dict = {}
#
#
# def fibonacci_number_naive(n):
#     assert 0 <= n <= 45
#     if n <= 1:
#         return n
#
#     return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)

def fibonacci_number_looping(n):
    assert 0 <= n <= 45
    fibonacci_number_list = [0,1]
    for i in range(2,n+1):
        fibonacci_number_list.append(fibonacci_number_list[i-1]+fibonacci_number_list[i-2])
    return fibonacci_number_list[n]

# def fibonacci_number(n):
#     assert 0 <= n <= 45
#     if n <= 1:  # base case of 0 or 1
#         return n
#     if n not in fibbo_dict:  # if we haven't already computed fibbonaci(n), add it to the dictionary
#         fibbo_dict[n] = fibonacci_number(n - 1) + fibonacci_number(n - 2)
#     return fibbo_dict[n]
#
#
# if __name__ == '__main__':
#     input_n = int(input())
#     print(fibonacci_number(input_n))

print(fibonacci_number_looping(50))
