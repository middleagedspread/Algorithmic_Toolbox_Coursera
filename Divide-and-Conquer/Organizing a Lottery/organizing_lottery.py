# python3
from sys import stdin
from bisect import bisect_left, bisect_right
import random

def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):

    # Use constants to help sort point and segment starts / ends
    LEFT = 0
    POINT = 1
    RIGHT = 2

    # Create a list of tuples (value, type) representing the points and line segments
    segments_and_points_array = []
    for start in starts:
        segments_and_points_array.append((start, LEFT))
    for end in ends:
        segments_and_points_array.append((end, RIGHT))
    for point in points:
        segments_and_points_array.append((point, POINT))

    # sort the array elements by value, then type
    segments_and_points_array.sort()

    score_count = 0

    # Initialise a dictionary to hold scores for each point
    point_scores = {}
    for point in points:
        point_scores[point] = 0

    # iterate through segments and points
    for i, tuple in enumerate(segments_and_points_array):
        if tuple[1] == 0:  # LEFT of segment - increment score:
            score_count += 1
        elif tuple[1] == 1:  # POINT - assign current score to point
            point_scores[tuple[0]] = score_count
        elif tuple[1] == 2:  # RIGHT of segment - decrement score
            score_count -= 1

    # return a list of point scores in the original point order
    return [point_scores[point] for point in points]


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)





