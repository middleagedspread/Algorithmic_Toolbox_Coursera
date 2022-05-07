# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def sort_key(n):  # sort order for largest number problem
    # assert 0 <= n < 10**3
    n = str(n)  #convert number to string
    if len(n) == 1:  # if a single digit number n
        return int(n + n + n)  # convert to three digit nnn
    elif len(n) == 2:  # if a 2 digit number nm
        return int(n + n[0])  # convert to three digit nmn
    elif len(n) == 3:  # if a three digit number nmo
        return int(n)  # return nmo
    elif len(n) == 4:  # if a four digit number 1000
        return 0.5  # return 0.5 so it comes before 0



def largest_number(numbers):  # parameter is list of integers 1<= n <= 999
    numbers.sort(key=sort_key, reverse=True)  # sort descending by sort function
    largest = list(map(str, numbers))  # convert integer list to list of strings
    largest = "".join(largest)  # concatenate
    return int(largest)  # return as an integer


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))

#
# print(largest_number_naive([0, 11, 13, 111, 113, 131, 132, 133, 1000]))
# print(largest_number([0, 11, 13, 111, 113, 131, 132, 133, 1000]))
