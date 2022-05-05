# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

# finds the minimum number of points such that all segments contain a point
def compute_optimal_points(segments):
    # sort the segments by rightmost point, ascending
    # print(segments)
    # segments.sort(key=lambda x: (x.end, -x.start))
    segments.sort(key=lambda x: x.end)  # O (n log n)
    # print(segments)
    next_point = segments[0].end
    points = [next_point]
    # print(next_point)
    for i in range(1,len(segments)):  # O(n)
        # if the point doesn't overlap this segment
        if not (segments[i].start <= next_point <= segments[i].end):
            # update next point to end of this segment and add to points
            next_point = segments[i].end
            points.append(next_point)

    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)

# print(compute_optimal_points([Segment(1, 3), Segment(2, 5), Segment(3, 6)]))
# print(compute_optimal_points([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]))

