# Task: 
# The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3 -Q1).

# Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements, 
#  construct a data set, S, where each Xi occurs at frequency Fi. Then calculate and print S's interquartile range, 
#   rounded to a scale of 1 decimal place (i.e., 12.3 format).

# Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, 
#  and be sure to not include the median in your upper and lower data sets.

# ---------------------------------------------- SOLUTION ---------------------------------------------------------- #

n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

x = []
for i in range(n):
    x += [data[i]] * freq[i]

N = sum(freq)
x.sort()

def median(x):
    if len(x) % 2 == 0:
        return int( (x[len(x)//2 - 1] +  x[len(x)//2]) / 2)
    else:
        return x[len(x)//2]
    
def quartiles(N, x):
    Q1 = median(x[:N//2])
    Q2 = median(x)
    if N % 2 == 0:
        Q3 = median(x[N//2: ])
    else:
        Q3 = median(x[N//2+1: ])
    return Q1, Q2, Q3
    
Q1,Q2,Q3 = quartiles(N,x)
iqr = round(float(Q3 - Q1),1)
print(iqr)

# --------------------------------------------- END SOLUTION -------------------------------------------------------- #
