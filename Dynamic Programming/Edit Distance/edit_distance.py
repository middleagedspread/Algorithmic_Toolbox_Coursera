# python3
import numpy as np

def edit_distance(target, source, type = "Levenshtein"):
    # function finds the edit distance (LCS distance - only deletions and insertions) between two strings O(n^2)
    # target is correct string
    # source is starting string
    # we add a hash mark at the beginning of each string so that solution_array(0,0) will equal 0
    target = "#" + target
    source = "#" + source

    # split strings into list of characters
    target = [c for c in target]
    source = [c for c in source]

    # build a matrix of len(source) rows, len(target) columns
    solution = np.zeros((len(source), len(target)))

    # e.g.:

    #   # t a r g e t
    # # 0 0 0 0 0 0 0
    # s 0 0 0 0 0 0 0
    # o 0 0 0 0 0 0 0
    # u 0 0 0 0 0 0 0
    # r 0 0 0 0 0 0 0
    # c 0 0 0 0 0 0 0
    # e 0 0 0 0 0 0 0

    # initialise first row, column with edit distances
    solution[0] = [index for index in range(len(target))]
    solution[:,0] = [index for index in range(len(source))]

    # e.g.:

    #   # t a r g e t
    # # 0 1 2 3 4 5 6
    # s 1 0 0 0 0 0 0
    # o 2 0 0 0 0 0 0
    # u 3 0 0 0 0 0 0
    # r 4 0 0 0 0 0 0
    # c 5 0 0 0 0 0 0
    # e 6 0 0 0 0 0 0

    # go through every column
    for column in range(1, len(target)):
      # go through every row
      for row in range(1, len(source)):

         if target[column] != source[row] and type == "Levenshtein":
            solution[row, column] = min(solution[row-1, column], solution[row, column-1], solution[row-1, column-1]) + 1
         elif target[column] != source[row] and type == "LCS":
            solution[row, column] = min(solution[row-1, column], solution[row, column-1]) + 1
         else:
            solution[row, column] = solution[row-1, column-1]

    # e.g.:

    #   # t a r g e t
    # # 0 1 2 3 4 5 6
    # s 1 2 3 4 5 6 7
    # o 2 3 4 5 6 7 8
    # u 3 4 5 6 7 8 9
    # r 4 5 6 5 6 7 8
    # c 5 6 7 6 7 8 9
    # e 6 7 8 7 8 7 8

    # return solution[-1][-1], solution
    return int(solution[-1][-1])


#
if __name__ == "__main__":
    print(edit_distance(input(), input()))

# string_1 = "there once was a ship that went to sea"
# string_2 = "and the name of the ship was the billy o tea"
#
# # string_1 = "ab" * 50
# # string_2 = "ba" * 50

# string_1, string_2 = "ab", "ab"
# string_1, string_2 = "short", "ports"
# string_1, string_2 = "editing", "distance"
# string_1, string_2 = "a" * 100, "a" * 100
# string_1, string_2 = "ab" * 50, "ba" * 50
#
# print(edit_distance(string_1, string_2, "Levenshtein"))
# # # print(edit_distance("editing", "distance", "LCS"))
