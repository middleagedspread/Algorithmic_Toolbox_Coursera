# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
import random
import time


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

# ________________________________


def min_between_array_distance(mid_strip, size, distance): # tested and demonstrated to run in O(n)
    # for each point in the mid-strip, get the distance to (up to) the next 7 points
    # in order of y coordinate. We only need to check 7 points because
    # at maximum 8 points can exist in a matrix of 8 squares (2 row x 4 column) each
    # of side 1/2 x sqrt(min_within_array_sqd_distance) without being closer to one another
    # than sqrt(min_within_array_sqd_distance) - a contradiction
    min_distance = distance
    # print(mid_strip)
    # print("size:", size)
    # print("distance:", distance)

    for i in range(size):  # check each point in the mid-strip O(n) time
        # print("i:",i)
        for j in range(i+1, min(size, i+7)): # compare with next 7 points
            # print("j:",j)
            # print("mid_strip[j][1]:", mid_strip[j][1])
            # print("mid_strip[i][1]:", mid_strip[i][1])
            if (mid_strip[j][1] - mid_strip[i][1]) < min_distance: # filter out if y-coords are > min_distance apart
                min_distance = min(min_distance, sqrt(distance_squared(mid_strip[i], mid_strip[j])))
    return min_distance


# Utility function to split the arrays left and right.
# Maintains order of indexed_by_y. Runs in O(n) time
def split_left_and_right(indexed_sorted_by_x, indexed_sorted_by_y, mid_x):
    # print("mid_x:", mid_x)
    # print("indexed_sorted_by_x[mid_x]:", indexed_sorted_by_x[mid_x])

    left_indexed_x = indexed_sorted_by_x[:mid_x]
    right_indexed_x = indexed_sorted_by_x[mid_x:]
    left_indexed_y = []
    right_indexed_y = []
    for point_and_index in indexed_sorted_by_y:
        # print("point_and_index:", point_and_index)
        # print("point_and_index[0]:", point_and_index[0])
        # print("point_and_index[0][0]:", point_and_index[0][0])
        # print("mid_x x coordinate:", indexed_sorted_by_x[mid_x][0][0])
        if point_and_index[1] < indexed_sorted_by_x[mid_x][1]:
            # print(point_and_index, "goes left")
            left_indexed_y.append(point_and_index)
        else:
            # print(point_and_index, "goes right")
            right_indexed_y.append(point_and_index)
    return left_indexed_x, right_indexed_x, left_indexed_y, right_indexed_y


def minimum_distance_squared(points):

    # One time operation to sort points by x and y, adding the sorted_by_x index to both
    sorted_by_x = sorted(points, key=lambda x: (x[0], x[1])) # sort by first (x) element of tuple O(nlogn) time
    indexed_sorted_by_x = []
    for i in range(len(sorted_by_x)):
        indexed_sorted_by_x.append([sorted_by_x[i],i])
    indexed_sorted_by_y = sorted(indexed_sorted_by_x, key=lambda x: x[0][1]) # sort by second (y) element of tuple O(nlogn) time



    def min_dist_sqd_partition(indexed_sorted_by_x, indexed_sorted_by_y):

        mid_x = len(indexed_sorted_by_x) //2
        if len(indexed_sorted_by_x) <= 1:
            return float("inf")
        elif len(indexed_sorted_by_x) == 2:
            # print(distance_squared(indexed_sorted_by_x[0][0], indexed_sorted_by_x[1][0]))
            return distance_squared(indexed_sorted_by_x[0][0], indexed_sorted_by_x[1][0])
        else:
            # recursive calls to get minimum within-half-array distance O(log n) time
            left_x, right_x, left_y, right_y = split_left_and_right(indexed_sorted_by_x, indexed_sorted_by_y, mid_x)
            # print("left_x:", left_x)
            # print("left_y:", left_y)
            # print("right_x:", right_x)
            # print("right_y:", right_y)
            min_left_sqd_distance = min_dist_sqd_partition(left_x, left_y)
            # print("min_left_sqd_distance:", min_left_sqd_distance)
            min_right_sqd_distance = min_dist_sqd_partition(right_x, right_y)
            # print("min_right_sqd_distance:", min_right_sqd_distance)

        min_within_array_sqd_distance = min(min_right_sqd_distance, min_left_sqd_distance)
        min_distance = sqrt(min_within_array_sqd_distance)
        # print("min_within_array_sqd_distance:", min_within_array_sqd_distance)

        # now get the minimum between-half-array distance
        # find the midpoint between the far left and far right elements

        mid_line_x_coord = (indexed_sorted_by_x[mid_x][0][0] + indexed_sorted_by_x[mid_x+1][0][0]) / 2
        # print("mid_line_x_coord:",mid_line_x_coord)
        # print("minimum x coord:", mid_line_x_coord-sqrt(min_within_array_sqd_distance))
        # print("maximum x coord:", mid_line_x_coord+sqrt(min_within_array_sqd_distance))

        # define a strip of width 2 x sqrt(min_within_array_sqd_distance) centred on midline
        # and get a list of points in that strip from the sorted-by-y array
        mid_strip_points = [point[0] for point in indexed_sorted_by_y if mid_line_x_coord-min_distance <= point[0][0] <= mid_line_x_coord+min_distance]
        size = len(mid_strip_points)
        # print("mid_strip_points:",mid_strip_points)

        between_array_distance = min_between_array_distance(mid_strip_points, size, min_distance)
        between_array_distance_sqd = between_array_distance * between_array_distance


        return min(min_within_array_sqd_distance, between_array_distance_sqd)

    return min_dist_sqd_partition(indexed_sorted_by_x, indexed_sorted_by_y)
# ________________________________



# if __name__ == '__main__':
#     input_n = int(input())
#     input_points = []
#     for _ in range(input_n):
#         x, y = map(int, input().split())
#         input_point = Point(x, y)
#         input_points.append(input_point)
#
#     print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
# #




# testing_points = [Point(4, 4), Point(-2, -2), Point(-3, -4), Point(-1, 3), Point(2, 3), Point(-4, 0), Point(1, 1), Point(-1, -1), Point(3, -1), Point(-4, 2), Point(-2, 4)]
# testing_points = [Point(-9, -2), Point(-4, -8), Point(-4, -1), Point(-1, 7), Point(1, 10), Point(1, 6)]
# # testing_points = [Point(0, 0), Point(3, 4), Point(5, 4)]
# testing_points = [Point(-3, -4), Point(-2, -2), Point(-2, 4)]
# print(sqrt(minimum_distance_squared_naive(testing_points)))
# print(sqrt(minimum_distance_squared(testing_points)))

def generate_test_cases(TEST_LENGTH=10, number_of_tests=10):
    all_tests = []
    for i in range(number_of_tests):
        all_tests.append([])
        lst1 = [random.randint(-10**9, 10**9) for i in range(TEST_LENGTH)]
        lst2 = [random.randint(-10**9, 10**9) for i in range(TEST_LENGTH)]
        for j in range(TEST_LENGTH):
            all_tests[i].append(Point(lst1[j], lst2[j]))
    return all_tests
#
# def generate_test_mid_strips(TEST_LENGTH = 100, number_of_tests = 10):
#     all_mid_strips=[]
#     for i in range(number_of_tests):
#         all_mid_strips.append([])
#         lst1 = [random.randint(-10, 10) for i in range(TEST_LENGTH)]
#         lst2 = [random.randint(-10**9, 10**9) for i in range(TEST_LENGTH)]
#         for j in range(0,TEST_LENGTH-1):
#             all_mid_strips[i].append(Point(lst1[j], lst2[j]))
#     sorted_by_y = sorted(all_mid_strips, key=lambda x: x[1]) # sort by second (y) element of tuple O(nlogn) time
#     return sorted_by_y

number_of_tests = 100
TEST_LENGTH = 10000
# distance = 1000000000
#
list_of_big_points = generate_test_cases(TEST_LENGTH, number_of_tests)
# list_of_midstirps = generate_test_mid_strips(TEST_LENGTH, number_of_tests)
#
#
tic = time.perf_counter()
for i in range(number_of_tests):
    print(sqrt(minimum_distance_squared(list_of_big_points[i])))
    # print(min_between_array_distance(list_of_midstirps[i], TEST_LENGTH-1, distance))
toc = time.perf_counter()
print(f"Ran {number_of_tests} test cases of length {TEST_LENGTH} in {toc - tic:0.8f} seconds")
print(f"Average time of {((toc - tic) / number_of_tests) } seconds")



# points = [Point(4, 4), Point(-2, -2), Point(-3, -4), Point(-1, 3), Point(2, 3), Point(-4, 0), Point(1, 1), Point(-1, -1), Point(3, -1), Point(-4, 2), Point(-2, 4)]
# sorted_by_x = sorted(points, key=lambda x: x[0]) # sort by first (x) element of tuple O(nlogn) time
# indexed_sorted_by_x = []
# for i in range(len(sorted_by_x)):
#     indexed_sorted_by_x.append([sorted_by_x[i],i])
# print(indexed_sorted_by_x)
# indexed_sorted_by_y = sorted(indexed_sorted_by_x, key=lambda x: x[0][1]) # sort by second (y) element of tuple O(nlogn) time
# print(indexed_sorted_by_y)
#
# mid_x = len(indexed_sorted_by_x) //2
# mid_point = indexed_sorted_by_x[mid_x]
# left_indexed_x = indexed_sorted_by_x[:mid_x]
# right_indexed_x = indexed_sorted_by_x[mid_x:]
# left_indexed_y = []
# right_indexed_y = []
# print(left_indexed_x)
# print(right_indexed_x)
# for point_and_index in indexed_sorted_by_y:
#     if point_and_index[1] < mid_x:
#         left_indexed_y.append(point_and_index)
#     else:
#         right_indexed_y.append(point_and_index)
#
# print(left_indexed_y)
# print(right_indexed_y)

# left_x = [[Point(x=-4, y=0), 0], [Point(x=-4, y=2), 1]]
# left_y = [[Point(x=-4, y=0), 0], [Point(x=-4, y=2), 1]]
# right_x = [[Point(x=-3, y=-4), 2], [Point(x=-2, y=-2), 3], [Point(x=-2, y=4), 4]]
# right_y = [[Point(x=-3, y=-4), 2], [Point(x=-2, y=-2), 3], [Point(x=-2, y=4), 4]]
# left_x = [[Point(x=-1, y=-1), 5], [Point(x=-1, y=3), 6], [Point(x=1, y=1), 7]]
# left_y = [[Point(x=-1, y=-1), 5], [Point(x=1, y=1), 7], [Point(x=-1, y=3), 6]]

# testing_points = [Point(4, 4), Point(-2, -2), Point(-3, -4), Point(-1, 3), Point(2, 3), Point(-4, 0), Point(1, 1), Point(-1, -1), Point(3, -1), Point(-4, 2), Point(-2, 4)]
# sorted_by_x = sorted(testing_points, key=lambda x: (x[0], x[1])) # sort by first (x) element of tuple O(nlogn) time
# indexed_sorted_by_x = []
# for i in range(len(sorted_by_x)):
#     indexed_sorted_by_x.append([sorted_by_x[i],i])
# indexed_sorted_by_y = sorted(indexed_sorted_by_x, key=lambda x: x[0][1]) # sort by second (y) element of tuple O(nlogn) time
#
# print("indexed_sorted_by_x:", indexed_sorted_by_x)
# print("indexed_sorted_by_y:", indexed_sorted_by_y)
#
#
# left_x, right_x, left_y, right_y = split_left_and_right(indexed_sorted_by_x, indexed_sorted_by_y, len(indexed_sorted_by_x)//2)

# length = len(left_x)
# left_x, right_x, left_y, right_y = split_left_and_right(left_x, left_y, length //2)
# length = len(right_x)
# left_x, right_x, left_y, right_y = split_left_and_right(right_x, right_y, length//2)

#
# print("left_x:", left_x)
# print("left_y:", left_y)
# print("right_x:", right_x)
# print("right_y:", right_y)
