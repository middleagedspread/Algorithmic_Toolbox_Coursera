# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    first_sequence_length = len(first_sequence)
    second_sequence_length = len(second_sequence)
    third_sequence_length = len(third_sequence)

    # initialise 3d table to hold the longest common sub-sequence length at
    # any intercept point
    
    lcs_table = [[[0 for x in range(third_sequence_length+1)] for x in range(second_sequence_length+1)] for x in range(first_sequence_length+1)]
    
    # e.g. 3d version of
    #   0 A B C D
    # 0 0 0 0 0 0
    # A 0 0 0 0 0
    # C 0 0 0 0 0
    # D 0 0 0 0 0
    
    # walk through the matrix comparing the subsequences of the sequences to that point
    # and recording the lcs length at every point
    for i in range(first_sequence_length+1):
        for j in range(second_sequence_length+1):
            for k in range(third_sequence_length+1):
                if i == 0 or j == 0 or k == 0:  # one of the sub-sequences is of zero length
                    lcs_table[i][j][k] = 0  # therefore there can be no common subsequence and lcs length is 0
                elif first_sequence[i-1] == second_sequence[j-1] == third_sequence[k-1]:  # if the 'characters' of the sequences match at this point
                    lcs_table[i][j][k] = lcs_table[i-1][j-1][k-1]+1  # increment this sub-sequence length
                else:
                    # copy length of longest sub-sequence up to this point
                    lcs_table[i][j][k] = max(lcs_table[i-1][j][k], lcs_table[i][j-1][k], lcs_table[i][j][k-1])
    

    # e.g. 3d version of
    #   0 A B C D
    # 0 0 0 0 0 0
    # A 0 1 1 1 1
    # C 0 1 1 2 2
    # D 0 1 1 2 3
    
    # now that we have found the longest sub-sequence length at every point
    # in the matrix formed by the intercepts of the sequences
    # we can walk back through the table and the sequences
    # identifying a (possibly arbitrary) longest sub-sequence
    
    # length of the longest common sub-sequence held in last cell
    lcs_length = lcs_table[first_sequence_length][second_sequence_length][third_sequence_length]
    
    # # set index to length of longest common sub-sequence
    # index = lcs_length
    #
    # # create a list to hold the lcs
    # lcs_list = [""] * index
    #
    # # initialise indices to last character of sequences
    # i = first_sequence_length
    # j = second_sequence_length
    # k = third_sequence_length
    #
    # while i > 0 and j > 0 and k > 0:  # walk backwards through the lcs_table
    #     if first_sequence[i-1] == second_sequence[j-1] and second_sequence[j-1] == third_sequence[k-1]:  # if the characters match they are part of a common sub-sequence
    #         lcs_list[index-1] = first_sequence[i-1]  # add the character to the lcs list
    #         index -= 1  # move backwards in the lcs_list
    #         # move diagonally up in the table / back by one character in each sequence
    #         i -= 1
    #         j -= 1
    #         k -= 1
    #     # if the characters in the sequence don't match we move backwards through
    #     # the sequences according to which direction in the lcs_table has the longest
    #     # sub-sequence
    #     elif lcs_table[i-1][j][k] > lcs_table[i][j-1][k] and lcs_table[i-1][j][k] > lcs_table[i][j][k-1]:  # if the longest sub-sequence is in the i direction
    #         i -= 1
    #     elif lcs_table[i][j-1][k] > lcs_table[i-1][j][k] and lcs_table[i][j-1][k] > lcs_table[i][j][k-1]:  # if the longest sub-sequence is in the j direction
    #         j -= 1
    #     else:  # if the longest sub-sequence is in the k direction, or both are equally long
    #         k -= 1
    
    return lcs_length


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
