# python3
import time

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




if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))

