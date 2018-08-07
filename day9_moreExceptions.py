# Task
# Write a Calculator class with a single method: int power(int,int). 
# The power method takes two integers,n and p, as parameters and returns the integer result of n^p. 
# If either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.

# Note: Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.

# ------------------------------------------------ Solution ------------------------------------------------------------

# Simple and Straight-forward approach to the challenge
# Creating Calculator class
class Calculator:
    # Creating class method
    def power(self, n, p):
        if (n>0) and (p>0):
            return n**p
        # Raising exception when n and p are not positive
        else:
            raise Exception("n and p should be non-negative")
            
# ------------------------------------------------ End Solution ----------------------------------------------------------

# -------------------------------- HackerRank Calculator Instance Creation and Input -------------------------------------

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
        
# --------------------------------------------------- End File -----------------------------------------------------------
