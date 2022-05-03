# python3
#import time

def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d


    stops.append(d)
    min_stops = 0
    current_position = 0
    while current_position + m < d:
        index = len(stops)-1
        while stops[index] > current_position + m:
            index -=1
        if current_position == stops[index]:
            return -1
        current_position = stops[index]
        min_stops +=1
    return min_stops
#


def refills(distance, gas_range, stops, location=0):
    # print(f"distance: {distance}")
    # print(f"stops[0] - location: {stops[0] - location}")
    # print(f"gas range: {gas_range}")
    # print(f"stops: {stops}")
    # print(f"location: {location}")

    if location + gas_range >= distance:
        return 0

    if not stops or stops[0] - location > gas_range: # impossible journey
        return -1

    last_stop = location

    while stops and (stops[0] - location <= gas_range):
        last_stop = stops[0]
        stops.pop(0)

    next_stop = refills(distance, gas_range, stops, last_stop)
    if next_stop == -1:
        return -1
    else:
        return 1 + next_stop


def compute_min_number_of_refills_theirs(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    return refills(d, m, stops)


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))

# tic = time.perf_counter()
# print(compute_min_number_of_refills(500, 200, [100, 200, 300, 400]))
# print(compute_min_number_of_refills(950, 400, [200, 375, 550, 750]))
# print(compute_min_number_of_refills(10, 3, [1, 2, 5, 9]))
# print(compute_min_number_of_refills(200, 250, [100, 150]))
# print(compute_min_number_of_refills(100, 120, [30, 60, 80]))
# toc = time.perf_counter()
# print(f"Ran the code in {toc - tic:0.8f} seconds")
#
# tic = time.perf_counter()
# print(compute_min_number_of_refills_theirs(500, 200, [100, 200, 300, 400]))
# print(compute_min_number_of_refills_theirs(950, 400, [200, 375, 550, 750]))
# print(compute_min_number_of_refills_theirs(10, 3, [1, 2, 5, 9]))
# print(compute_min_number_of_refills_theirs(200, 250, [100, 150]))
# print(compute_min_number_of_refills_theirs(100, 120, [30, 60, 80]))
# toc = time.perf_counter()
# print(f"Ran the code in {toc - tic:0.8f} seconds")

