# Task:
#  Given an array, , of integers, calculate and print the standard deviation. 
#   Your answer should be in decimal form, rounded to a scale of decimal place (i.e., format). 
#    An error margin of will be tolerated for the standard deviation.


# ------------- SOLUTION ------------- #

n = int(input())
X = [int(x) for x in input().split()]

mean = sum(X) / n
vars = []
for i in X:
    vars.append((i - mean)**2)
total_vars = sum(vars)
avgvars = total_vars / n
sd = round(avgvars**(1/2),1)
print(sd)

# ------------ END SOLUTION ------------- #

