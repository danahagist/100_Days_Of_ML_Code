# Task: Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, 
# calculate and print the weighted mean of X's elements. 
# Your answer should be rounded to a scale of 1 decimal place (i.e.,12.3 format).


# ----------------------------- Solution -------------------------------------------------------------

# Creating weighted mean function, taking parameters x (array of values) and w (weights)
def weighted_mean(x,w):
    # Initializing variables for numerator and denominator of weighted mean function
    sum_weighted_values = 0
    sum_weights = 0
    # Iterating over values in N (length of array)
    for i in range(N):
        # Adding weighted values (numerator)
        sum_weighted_values += x[i] * w[i]
        # Adding weighted sums (denominator)
        sum_weights += w[i]
    # Calculating weigted mean (numerator/denominator)
    return sum_weighted_values / sum_weights

# Reading input lines
N = int(input())
x = [int(value) for value in input().split()]
w = [int(value) for value in input().split()]

# Printing rounded, weighted mean
print(round(weighted_mean(x, w), 1))

# --------------------------- End Solution -----------------------------------------------------------
