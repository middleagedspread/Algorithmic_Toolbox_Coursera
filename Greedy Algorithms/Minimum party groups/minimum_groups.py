#  python 3

# computes minimum number of groups of children such that no child in a
# group is more than a year older than any other child in that group

def compute_min_number_of_groups(number_of_children, children_ages):
    assert 1 <= number_of_children <= 10 ** 5
    assert all(children_ages[i] > 0.0 for i in range(len(children_ages) - 1))

    children_ages.sort()  # O n log n
    number_of_groups = 1
    youngest_in_group = children_ages[0]

    for i in range(0,len(children_ages)): #  O(n)
        if children_ages[i] > youngest_in_group + 1.0:
            number_of_groups += 1
            youngest_in_group = children_ages[i]

    return number_of_groups

print(compute_min_number_of_groups(2,[5.0,6.5]))
print(compute_min_number_of_groups(6, [5.5, 6.1, 6.4, 6.6, 7.0, 7.8]))
print(compute_min_number_of_groups(2, [7.2, 7.6]))
print(compute_min_number_of_groups(4, [5.0, 6.1, 7.2, 8.3]))
print(compute_min_number_of_groups(5, [5.0, 6.0, 7.0, 8.0, 9.0]))




