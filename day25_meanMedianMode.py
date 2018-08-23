# Task: Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
#  If your array contains more than one modal value, choose the numerically smallest one.

# ------------------------------------ Solution ---------------------------------------------------------- #

# Reading length of the array, which is first input line
N = int(input())

# Taking array as input, splitting and storing values as integers
x = [int(x) for x in input().split()]

# Creating mean function, returning sum of array divided by length of array
# round function is rounding to 1 decimal value
def mean(x):
    return round(sum(x) / N, 1)

# Creating median function to find value in middle of distribution
def median(x):
    # Sorting x, which is required to know where the 'middle value' is
    x = sorted(x)
    # Returning middle value when odd-numbered length of array
    if N % 2 != 0:
        return round(x[N//2],1)
    # Returning average of 2 middle values when even-numbered length of array
    else:
        return round(((x[N//2] + x[N//2 - 1]) / 2),1)

# Creating mode function to find value that shows up the most in distribution
def mode(x):
    # Initializing a current, count, and max to use for determining the most frequent value
    current = 0
    count = 0
    max = 0
    # Sorting x so that lowest value will return if there is no mode
    # Also, the process below will ONLY work if values are sorted first
    x = sorted(x)
    # Iterating through values in x to find most frequent value
    for i in x:
        # Increasing count if i is equal to current (this works because we are sorted)
        if i == current:
            count += 1
        # When i is not equal to current, starting count at 1 and setting current value to i
        else:
            count = 1
            current = i
        # When count greater than the max count, setting max to count and mode to i
        if (count > max):
            max = count
            mode = i
        # Returning the mode
        return mode

# Checking with pandas for value counts, to determine if there is a mode
print(pd.value_counts(x))
# Results show max value count is 1, so lowest value should be returned
            
print(mean(x))
print(median(x))
print(mode(x))

# ----------------------------- End Solution ----------------------------------------------------- #
