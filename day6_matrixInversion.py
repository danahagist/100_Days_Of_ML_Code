# Below is how you would find the inverse of a matrix,
# multiply the inverse matrix by the original matrix,
# and end up with an identity matrix

# Creating original matrix
matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])

# Defining matrix inversion equation
def matrix_inverse_two(m):
    det = (m[0,0]*m[1,1] - m[0,1]*m[1,0])
    if det == 0:
        return ValueError("error")
    right_m = np.asarray([
        [m[1,1], -m[0,1]],
        [-m[1,0], m[0,0]]
    ])
    inv_mat = np.dot(1/det, right_m)
    return inv_mat
 
# Applying matrix inversion to the original matrix
inverse_a = matrix_inverse_two(matrix_a)

# Multiplying inverted matrix by original matrix
i_2 = np.dot(inverse_a, matrix_a)

# Displaying the resulting identity matrix
print(i_2)
