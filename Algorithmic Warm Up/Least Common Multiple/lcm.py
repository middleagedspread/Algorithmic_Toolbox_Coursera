# python3
# import time


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


# def lcm(a, b):
#     assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
#     larger, smaller = max(a,b), min(a,b)
#     multiple = larger
#     while multiple % smaller != 0:
#         multiple += larger
#     return multiple

def gcd(a, b):  # Euclid's algorithm for finding the GCD of two numbers
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    if b == 0:  # no remainder on previous recursion
        return a  # the GCD
    else:
        a_prime = a % b  # a_prime is the remainder left when b divides a
        return gcd(b, a_prime)  # recursion

def lcm(a, b):  # using Euclid's GCD
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    larger, smaller = max(a,b), min(a,b)
    return int(smaller * larger / gcd(larger,smaller))

if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))

# tic = time.perf_counter()
# print(lcm_euclid(12345678,87654321))
# toc = time.perf_counter()
#
# print(f"lcm_euclid Ran in {toc - tic:0.8f} seconds")
#
# tic = time.perf_counter()
# print(lcm(12345678,87654321))
# toc = time.perf_counter()
#
# print(f"lcm ,ran in {toc - tic:0.8f} seconds")
