#Task
# Given a 6 x 6 2D Array, A:
# Calculate the hourglass sum for every hourglass in A.
# Print the maximum hourglass sum.

# Solution Set
# Assigning the above dimension to a variable
arr_dim = len(arr)

# Creating minimum (starting maximum) sum based on instructions
# Range of each value in A is -9 to 9, inclusive
# 7 is number of values in each hourglass
max_sum = -9 * 7

# Iterating through each row and column to the arr_dim - 2 position
# This is because the top and bottom of hourglass are 2 spaces wide
for row in range(arr_dim-2):
    for col in range(arr_dim-2):
        # Naming each position as hg (hourglass) and position in hourglass
        hg00 = arr[row][col]
        hg01 = arr[row][col+1]
        hg02 = arr[row][col+2]
        hg11 = arr[row+1][col+1]
        hg20 = arr[row+2][col]
        hg21 = arr[row+2][col+1]
        hg22 = arr[row+2][col+2]
        hg_sum = hg00 + hg01 + hg02 + hg11 + hg20 + hg21 + hg22
        # Determining whether this hourglass is the maximum sum
        if hg_sum > max_sum:
            max_sum = hg_sum
    
# Printing maximum sum
print(max_sum)
