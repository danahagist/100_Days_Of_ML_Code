# Task:
# The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n)...
# ...method are provided for you in the editor below.

# Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. 
# The implementation for the divisorSum(n) method must return the sum of all divisors of .

# ----------------------- HackerRank Creates AdvancedArithmetic Class -------------------------------

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
        
# ----------------------------------------- Solution ------------------------------------------------

class Calculator(AdvancedArithmetic):
    # Creating divisorSum method
    def divisorSum(self, n):
        # Creating empty list for divisors
        divisor = []
        # Iterating over entire range in n and...
        # ...adding all even divisors to the divisor list
        for index in range(1, n+1):
            if n % index == 0:
                divisor.append(index)
        else:
            pass
        # Returning sum of divisor list
        return sum(divisor)
        
# ---------------------------------------- End Solution -----------------------------------------------

# --------------------------------------- HackerRank Input --------------------------------------------
        
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

# -------------------------------------------- End File -----------------------------------------------
        
