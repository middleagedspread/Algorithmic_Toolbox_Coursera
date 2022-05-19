import unittest
import random
from organizing_lottery import points_cover, points_cover_naive


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([0, 5, 10], [3, 8, 13], [1, 17, 7])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):

        starts = []
        ends = []
        points = []

        # add values
        for segment in range(1,10):
            i, j, point = random.randint(1,100), random.randint(1,100), random.randint(1,100)
            if i >= j:
                start, end = j, i
            else:
                start, end = i, j
            starts.append(start)
            ends.append(end)
            points.append(point)

        print(starts, ends, points)

        self.assertEqual(points_cover(starts, ends, points),
                             points_cover_naive(starts, ends, points))

    # def test_large(self):
    #     type here


if __name__ == '__main__':
    unittest.main()
