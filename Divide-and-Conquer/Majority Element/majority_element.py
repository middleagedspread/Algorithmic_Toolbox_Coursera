# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5


    def decide_majority(left, right):
        if left == right:  # return if single element
            return elements[left]
        midpoint = (right - left) // 2 + left
        left_majority = decide_majority(left, midpoint)  # recursive call on left half
        right_majority = decide_majority(midpoint+1, right)   # recursive call on right half

        if left_majority == right_majority:  # if the majority element from each half matches, return it
            return left_majority

        #  otherwise count across the combined array for a majority element
        left_count = sum(1 for i in range(left, right+1) if elements[i] == left_majority)
        right_count = sum(1 for i in range(left, right+1) if elements[i] == right_majority)

        if left_count > right_count:
            return left_majority
        else:
            return right_majority

    # decide majority may return an element with count = n/2
    candidate = decide_majority(0, len(elements)-1)
    candidate_count = sum(1 for i in range(0,len(elements)) if elements[i] == candidate)
    if candidate_count > (len(elements)/2):
        return 1
    else:
        return 0




if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))

# test_array = [1, 2, 2, 3, 1, 1, 2]
# print(majority_element(test_array))

