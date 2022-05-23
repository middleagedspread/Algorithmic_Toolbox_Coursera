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


def min_between_array_distance(mid_strip, size, distance):  # tested and demonstrated to run in O(n)
    # for each point in the mid-strip, get the distance to (up to) the next 7 points
    # in order of y coordinate. We only need to check 7 points because
    # at maximum 8 points can exist in a matrix of 8 squares (2 row x 4 column) each
    # of side 1/2 x sqrt(min_within_array_sqd_distance) without being closer to one another
    # than sqrt(min_within_array_sqd_distance) - a contradiction
    min_distance = distance

    for i in range(size):  # check each point in the mid-strip O(n) time
        # print("i:",i)
        for j in range(i+1, min(size, i+7)):  # compare with next 7 points
            # print("j:",j)
            # print("mid_strip[j][1]:", mid_strip[j][1])
            # print("mid_strip[i][1]:", mid_strip[i][1])
            if (mid_strip[j][1] - mid_strip[i][1]) < min_distance:  # filter out if y-coordinates are > min_distance apart
                min_distance = min(min_distance, sqrt(distance_squared(mid_strip[i], mid_strip[j])))
    return min_distance


# Utility function to split the arrays left and right.
# Maintains order of indexed_by_y. Runs in O(n) time,
# but called with recursively decreasing size of array, so O(log n)
def split_left_and_right(indexed_sorted_by_x, indexed_sorted_by_y, mid_x):
    # split indexed_by_x at mid_x point
    left_indexed_x = indexed_sorted_by_x[:mid_x]
    right_indexed_x = indexed_sorted_by_x[mid_x:]
    left_indexed_y = []
    right_indexed_y = []
    # split indexed_by_y checking index < mid_x point index
    for point_and_index in indexed_sorted_by_y:
        if point_and_index[1] < indexed_sorted_by_x[mid_x][1]:
            left_indexed_y.append(point_and_index)
        else:
            right_indexed_y.append(point_and_index)
    return left_indexed_x, right_indexed_x, left_indexed_y, right_indexed_y


def minimum_distance_squared(points):

    # One time operation to sort points by x and y, adding the sorted_by_x index to both
    # so that indexed_by_y can be filtered by the indexed_by_x index
    sorted_by_x = sorted(points, key=lambda x: (x[0], x[1]))  # sort by first (x) element of tuple O(n log n) time
    indexed_sorted_by_x = []
    for i in range(len(sorted_by_x)):
        indexed_sorted_by_x.append([sorted_by_x[i], i])
    indexed_sorted_by_y = sorted(indexed_sorted_by_x, key=lambda x: x[0][1])  # sort by second (y) element of tuple O(n log n) time

    def min_dist_sqd_partition(indexed_sorted_by_x, indexed_sorted_by_y):
        mid_x = len(indexed_sorted_by_x) // 2
        if len(indexed_sorted_by_x) <= 1:
            return float("inf")
        elif len(indexed_sorted_by_x) == 2:
            # print(distance_squared(indexed_sorted_by_x[0][0], indexed_sorted_by_x[1][0]))
            return distance_squared(indexed_sorted_by_x[0][0], indexed_sorted_by_x[1][0])
        else:
            # split indexed_sorted_by_x and indexed_sorted_by_y around mid_x point
            left_x, right_x, left_y, right_y = split_left_and_right(indexed_sorted_by_x, indexed_sorted_by_y, mid_x)
            # recursive calls to get minimum within-half-array distance O(log n) time
            min_within_array_sqd_distance = min(min_dist_sqd_partition(left_x, left_y), min_dist_sqd_partition(right_x, right_y))
            min_distance = sqrt(min_within_array_sqd_distance)

            # now get the minimum between-half-array distance
            # find the midpoint between the left and right arrays
            # mid_line_x_coord = (indexed_sorted_by_x[mid_x][0][0] + indexed_sorted_by_x[mid_x+1][0][0]) / 2
            mid_line_x_coord = (left_x[-1][0][0] + right_x[0][0][0]) / 2

            # define a strip of width 2 x min_distance centred on the midline
            # and get a list of points in that strip from the sorted-by-y array
            mid_strip_points = [point[0] for point in indexed_sorted_by_y if mid_line_x_coord-min_distance <= point[0][0] <= mid_line_x_coord+min_distance]
            size = len(mid_strip_points)

            between_array_distance = min_between_array_distance(mid_strip_points, size, min_distance)
            between_array_distance_sqd = between_array_distance * between_array_distance

            return min(min_within_array_sqd_distance, between_array_distance_sqd)

    return min_dist_sqd_partition(indexed_sorted_by_x, indexed_sorted_by_y)
# ________________________________


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))

