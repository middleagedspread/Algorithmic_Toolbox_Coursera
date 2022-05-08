# python3
# from random import randint

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def sort_key(num):  # sort order for largest number problem
    # assert 0 <= n < 10**3
    num = str(num)  # convert number to string
    if len(num) == 1:  # if a single digit number n
        return int(num + num + num)  # convert to three digit nnn
    elif len(num) == 2:  # if a 2 digit number nm
        if int(num[0]) < int(num[1]):  # nm where n < m
            return float(num + str(float(num[0])+0.1))  # convert nmn+0.1 so sorts in front of nmn
        elif int(num[0]) > int(num[1]):  # nm where n > m
            return float(num + str(float(num[0])-0.1))  # convert nmn-0.1 so sorts behind nmn
        else:  # nn
            return int(num+num[0])  # convert to three digit nnn
    elif len(num) == 3:  # if a three-digit number nmo
        return int(num)  # return nmo
    elif len(num) == 4:  # if a four-digit number 1000
        return 0.5  # return 0.5 so it comes before 0


def largest_number(numbers):  # parameter is list of integers 1<= n <= 999
    if len(numbers) == 1:
        return numbers[0]
    numbers.sort(key=sort_key, reverse=True)  # sort descending by sort function
    largest = list(map(str, numbers))  # convert integer list to list of strings
    largest = "".join(largest)  # concatenate
    return int(largest)  # return as an integer


# def largestNumber(array):
#     # If there is only one element in the list, the element itself is the largest element.
#     # Below if condition checks the same.
#     if len(array)==1:
#         return array[0]
#     # Below lines are code are used to find the largest element possible.
#     # First, we convert a list into a string array that is suitable for concatenation
#     for i in range(len(array)):
#         array[i]=str(array[i])
#     # [54,546,548,60]=>['54','546','548','60']
#     # Second, we find the largest element by swapping technique.
#     for i in range(len(array)):
#         for j in range(1+i,len(array)):
#             if array[j]+array[i]>array[i]+array[j]:
#                 array[i],array[j]=array[j],array[i]
#     # ['60', '548', '546', '54']
#     # Refer JOIN function in Python
#     result=''.join(array)
#     # Edge Case: If all elements are 0, answer must be 0
#     if(result=='0'*len(result)):
#         return 0
#     else:
#         return int(result)

if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))

#
# print(largest_number([131, 132, 133, 1000, 99, 998, 989, 997, 979, 987]))
# print(largestNumber([131, 132, 133, 1000, 99, 998, 989, 997, 979, 987]))
# print(largest_number([987, 979, 997, 989, 998, 99, 1000, 133, 132, 131]))
# print(largestNumber([987, 979, 997, 989, 998, 99, 1000, 133, 132, 131]))
# print(largest_number([1, 10, 11, 100, 101, 110, 111, 1000]))
# print(largestNumber([1, 10, 11, 100, 101, 110, 111, 1000]))
# print(largest_number([0, 0, 1, 10]))
# print(largestNumber([0, 0, 1, 10]))

# number_string_list_one = ['16', '161', '16', '40', '404', '40']
# number_list_one = [16, 161, 16, 40, 404, 40]
# number_string_list_two = ['89', '757', '75', '720', '510', '310', '284', '274', '130']
# number_list_two = [89, 757, 75, 720, 510, 310, 284, 274, 130]
#
#
# print(largest_number(number_string_list_one))
# print(largestNumber(number_string_list_one))
# print(largest_number(number_list_one))
# print(largestNumber(number_list_one))
# print(largest_number(number_string_list_two))
# print(largestNumber(number_string_list_two))
# print(largest_number(number_list_two))
# print(largestNumber(number_list_two))


# for n in range(1, 10):
#     for max_value in [10, 20, 100, 1000]:
#         for _ in range(1000):
#             numbers = [randint(1, max_value) for _ in range(n)]
#             numbers_copy = numbers.copy()
#             if largest_number(numbers) != largestNumber(numbers_copy):
#                 print("Fail")
#                 print(numbers)
#                 print(numbers_copy)
#                 for i in numbers:
#                     print(i, type(i))
#                 print(largest_number(numbers))
#                 print(type(largest_number(numbers)))
#                 print(largestNumber(numbers))
#                 print(type(largestNumber(numbers)))


# n = '40'
# m = '16'
#
# print(float(n + str(float(n[0])+0.1)))
# print(float(m + str(float(m[0])+0.1)))
