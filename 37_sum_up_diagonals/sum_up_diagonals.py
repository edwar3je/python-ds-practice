def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    #first take account of the length using len(matrix), then calculate the last index using it
    length = len(matrix)
    last_index = length - 1

    #using the last_index, begin to extract 4 pieces of data (the diagonals of the matrix)
    corner_1 = matrix[0][0]
    corner_2 = matrix[0][last_index]
    corner_3 = matrix[last_index][0]
    corner_4 = matrix[last_index][last_index]

    #return the sum of all 4 corners
    return corner_1 + corner_2 + corner_3 + corner_4

print(sum_up_diagonals([[1, 2],[30, 40]]))
print(sum_up_diagonals([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
