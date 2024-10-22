def zero_matrix(matrix):
    # if there is a 0 in the matrix, make the entire column and row that the 0 is in = to 0

    # create sets for rows and columns to get unique values of indecies.
    rows_to_zero = set()
    columns_to_zero = set()
    
    
    # get all points in matrix where 0 needs to be added
    for n in range(len(matrix)):
        for m in range(len(matrix[0])):
            if matrix[n][m] == 0:
                rows_to_zero.add(n)
                columns_to_zero.add(m)
                
    # from all the points in set row_to_zero, from index 0 - N, convert it all to 0
    for n in rows_to_zero:
        for m in range(len(matrix[0])):
            matrix[n][m] = 0
            
    # from all the points set in col_to_zero, from index 0 - M, convert all to 0
    for m in columns_to_zero:
        for n in range(len(matrix)):
            matrix[n][m] = 0
    
    return matrix
                
    
    
    
if __name__ == '__main__':
    print(zero_matrix(matrix = [[1, 2, 3, 4, 5],
                         [6, 7, 0, 8, 9],
                         [4, 3, 2, 1, 6]]))