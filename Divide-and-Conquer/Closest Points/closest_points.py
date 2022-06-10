# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
# import random
# import time

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

# _________________________________________________


# store Shortest solution here
Shortest = float("inf")


def euclidean_distance(first_point, second_point):
    # if these are the closest points, sets global Shortest variable
    global Shortest
    dx = abs(first_point.x-second_point.x)
    dy = abs(first_point.y-second_point.y)
    # only calculates if x and y distances are shorter than global Shortest
    if dx < Shortest and dy < Shortest:
        dist = sqrt(dx**2 + dy**2)
        if dist < Shortest:
            Shortest = dist


def brute_force(points):
    #  similar to minimum_distance_squared_naive function, but no return value
    for first_point, second_point in combinations(points, 2):
        euclidean_distance(first_point, second_point)


def find_closest_split_pair(sorted_by_x):
    points_count = len(sorted_by_x)
    mid_x = sorted_by_x[points_count // 2].x
    # consider only point that are no further than 'Shortest' distance from x
    remained_points = sorted([p for p in sorted_by_x if mid_x - Shortest < p.x < mid_x + Shortest], key=lambda p: p.y)  # sort by y - can we improve this?
    remained_count = len(remained_points)
    for i, p1 in enumerate(remained_points[:-1]):
        for p2 in remained_points[i+1:min(i+7, remained_count)]:
            euclidean_distance(p1, p2)


def find_closest(sorted_by_x):
    # perform brute force for 3 or 2 points
    points_count = len(sorted_by_x)
    if points_count <= 3:
        return brute_force(sorted_by_x)
    # split into two halves (x line) -> keep sorted by x and y
    mid = points_count // 2
    left_sorted_by_x, right_sorted_by_x = sorted_by_x[:mid], sorted_by_x[mid:]
    find_closest(left_sorted_by_x)
    find_closest(right_sorted_by_x)
    # check Shortest result of split pair
    find_closest_split_pair(sorted_by_x)


def minimum_distance_squared(points):
    global Shortest
    Shortest = float("inf")
    sorted_by_x = sorted(points, key=lambda n: (n.x, n.y))  # One time presort by x, then y O(n log n)
    find_closest(sorted_by_x)
    return Shortest*Shortest

# ______________________________________________________________________

# def min_between_array_distance(mid_strip, size, distance):  # tested and demonstrated to run in O(n)
#     # for each point in the mid-strip, get the distance to (up to) the next 7 points
#     # in order of y coordinate. We only need to check 7 points because
#     # at maximum 8 points can exist in a matrix of 8 squares (2 row x 4 column) each
#     # of side 1/2 x sqrt(min_within_array_
#     # sqd_distance) without being closer to one another
#     # than sqrt(min_within_array_sqd_distance) - a contradiction
#     min_distance = distance
#
#     for i in range(size):  # check each point in the mid-strip O(n) time
#         # print("i:",i)
#         for j in range(i+1, min(size, i+7)):  # compare with next 7 points
#             # print("j:",j)
#             # print("mid_strip[j][1]:", mid_strip[j][1])
#             # print("mid_strip[i][1]:", mid_strip[i][1])
#             if (mid_strip[j][1] - mid_strip[i][1]) < min_distance:  # filter out if y-coordinates are > min_distance apart
#                 min_distance = min(min_distance, sqrt(distance_squared(mid_strip[i], mid_strip[j])))
#     return min_distance
#
#
# # Utility function to split the arrays left and right.
# # Maintains order of indexed_by_y. Runs in O(n) time,
# # but called with recursively decreasing size of array, so O(log n)
# def split_left_and_right(indexed_sorted_by_x, indexed_sorted_by_y, mid_x):
#     # split indexed_by_x at mid_x point
#     left_indexed_x = indexed_sorted_by_x[:mid_x]
#     right_indexed_x = indexed_sorted_by_x[mid_x:]
#     left_indexed_y = []
#     right_indexed_y = []
#     # split indexed_by_y checking index < mid_x point index
#     for point_and_index in indexed_sorted_by_y:
#         if point_and_index[1] < indexed_sorted_by_x[mid_x][1]:
#             left_indexed_y.append(point_and_index)
#         else:
#             right_indexed_y.append(point_and_index)
#     return left_indexed_x, right_indexed_x, left_indexed_y, right_indexed_y
#
#
# def minimum_distance_squared(points):
#
#     # One time operation to sort points by x and y, adding the sorted_by_x index to both
#     # so that indexed_by_y can be filtered by the indexed_by_x index
#     sorted_by_x = sorted(points, key=lambda x: (x[0], x[1]))  # sort by first (x) element of tuple O(n log n) time
#     indexed_sorted_by_x = []
#     for i in range(len(sorted_by_x)):
#         indexed_sorted_by_x.append([sorted_by_x[i], i])
#     indexed_sorted_by_y = sorted(indexed_sorted_by_x, key=lambda x: x[0][1])  # sort by second (y) element of tuple O(n log n) time
#
#     def min_dist_sqd_partition(indexed_sorted_by_x, indexed_sorted_by_y):
#         mid_x = len(indexed_sorted_by_x) // 2
#         if len(indexed_sorted_by_x) <= 1:
#             return float("inf")
#         elif len(indexed_sorted_by_x) <= 3:
#             # print(distance_squared(indexed_sorted_by_x[0][0], indexed_sorted_by_x[1][0]))
#             return minimum_distance_squared_naive([x[0] for x in indexed_sorted_by_x])
#             # return distance_squared(indexed_sorted_by_x[0][0], indexed_sorted_by_x[1][0])
#         else:
#             # split indexed_sorted_by_x and indexed_sorted_by_y around mid_x point
#             left_x, right_x, left_y, right_y = split_left_and_right(indexed_sorted_by_x, indexed_sorted_by_y, mid_x)
#             # recursive calls to get minimum within-half-array distance O(log n) time
#             min_within_array_sqd_distance = min(min_dist_sqd_partition(left_x, left_y), min_dist_sqd_partition(right_x, right_y))
#             min_distance = sqrt(min_within_array_sqd_distance)
#
#             # now get the minimum between-half-array distance
#             # find the midpoint between the left and right arrays
#             # mid_line_x_coord = (indexed_sorted_by_x[mid_x][0][0] + indexed_sorted_by_x[mid_x+1][0][0]) / 2
#             mid_line_x_coord = (left_x[-1][0][0] + right_x[0][0][0]) / 2
#
#             # define a strip of width 2 x min_distance centred on the midline
#             # and get a list of points in that strip from the sorted-by-y array
#             mid_strip_points = [point[0] for point in indexed_sorted_by_y if mid_line_x_coord-min_distance <= point[0][0] <= mid_line_x_coord+min_distance]
#             size = len(mid_strip_points)
#
#             between_array_distance = min_between_array_distance(mid_strip_points, size, min_distance)
#             between_array_distance_sqd = between_array_distance * between_array_distance
#
#             return min(min_within_array_sqd_distance, between_array_distance_sqd)
#
#     return min_dist_sqd_partition(indexed_sorted_by_x, indexed_sorted_by_y)
# # ________________________________


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))

# # ________________________________


# def generate_test_cases(test_length=10, number_of_tests=10):
#     all_tests = []
#     x_bound_low = -10**9
#     x_bound_high = 10**9
#     y_bound_low = -10**9
#     y_bound_high = 10**9
#
#     for i in range(number_of_tests):
#         all_tests.append([])
#         lst1 = [random.randint(x_bound_low, x_bound_high) for i in range(test_length)]
#         lst2 = [random.randint(y_bound_low, y_bound_high) for i in range(test_length)]
#         for j in range(test_length):
#             all_tests[i].append(Point(lst1[j], lst2[j]))
#     return all_tests
#
#
# number_of_tests = 1
# TEST_LENGTH = 1000000
#
# list_of_big_points = generate_test_cases(TEST_LENGTH, number_of_tests)
#
# tic = time.perf_counter()
# for i in range(number_of_tests):
#     print(sqrt(minimum_distance_squared(list_of_big_points[i])))
# toc = time.perf_counter()
# print(f"Ran {number_of_tests} tests of length {TEST_LENGTH} in {(toc - tic)} seconds")
# print(f"Average test time: {(toc - tic) / number_of_tests} seconds")
