# Task: Given an array, X, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3). 
#  It is guaranteed that Q1, Q2, Q3 and are integers.

# -------------------------- Solution ---------------------------------------------------

# Creating median function
def median(x):
    # Handling case where lengh of array is even (have to find mean of 2 middle values)
    if len(x) % 2 == 0:
        return int( (x[len(x)//2 - 1] +  x[len(x)//2]) / 2)
    # Handling case where length of array is odd (taking middle value)
    else:
        return x[len(x)//2]
   
# Creating quartiles function
def quartiles(N, x):
    # Q1 will take the middle value of the array up to the median
    Q1 = median(x[:N//2])
    # Q2 is finding the median of the array as defined above
    Q2 = median(x)
    # Q3 will be derived a little bit differently between the even and odd length case
    # This is because we are using flooring division, so in case where array length is odd, we have to add one
    if N % 2 == 0:
        Q3 = median(x[N//2: ])
    else:
        Q3 = median(x[N//2+1: ])
    return Q1, Q2, Q3
    
# Inputting N, x, and finding/printing quartiles
N = int(input())
x = sorted([int(i) for i in input().split()])
Q1,Q2,Q3 = quartiles(N,x)
print(Q1)
print(Q2)
print(Q3)

# -------------------------- End Solution -------------------------------------------------
