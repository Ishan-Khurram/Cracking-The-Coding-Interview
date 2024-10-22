def rotate_matrix(matrix):
    """
    THIS WORKS, BUT DOES NOT SATISFY THE CONDITION OF US CHANGING THE SAME MATRICIES.
    """
    # matrix_1 = []
    # for i in range(0, 5):
    #     new_row = []
    #     for k in range(4, -1, -1):
    #         new_row.append(matrix[k][i])
    #     matrix_1.append(new_row)

    # return matrix_1
    
    """
    NEW SOLUTION, BY ADJUSTING THE ORIGINAL MATRIX.
    """
    
    # change the first column into the first row.
    # for the question, you would normally use N instead of 5, but testing purposes.
    for i in range(0, 5):
        for k in range(i, 5): # increments as i changes.
            matrix[i][k], matrix[k][i] = matrix[k][i], matrix[i][k]
            
    # reverse the row to match the rotation.
    for i in range(5):
        matrix[i].reverse()
    
    return matrix

if __name__ == '__main__':
    print(rotate_matrix(matrix = [[5, 2, 9, 3, 7],
                                    [8, 4, 6, 1, 5],
                                    [1, 3, 7, 8, 6],
                                    [4, 9, 2, 7, 3],
                                    [6, 5, 8, 4, 1]]
        ))
    

"""
	1.	Swapping index points (this is called transposing the matrix), where you swap the element at position (i, j) with the element at (j, i) to turn rows into columns.
	2.	Reversing each row after the transposition, which aligns the elements in the correct order for the 90-degree clockwise rotation.
"""