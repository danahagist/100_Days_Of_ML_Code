# Task 
# Complete the Difference class by writing the following:

# A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
# A computeDifference method that finds the maximum absolute difference between any 2 numbers
#  in N and stores it in the maximumDifference instance variable.

# ------------------------- HackerRank creates Difference class ----------------------------------------------------

class Difference:
    def __init__(self, a):
        self.__elements = a


# -------------------------------------- Solution ------------------------------------------------------------------

    # Defining class method    
    def computeDifference(self):
        # setting the initial 'maximumDistance'
        self.maximumDifference = 0
        # Setting variable N to the length of a (our list input)
        N = len(a)
        # loop from 0 to lenth of N for first value
        for i in range(0,N):
            # loop from i+1 (next position to loop above) to length of N for second value
            for j in range(i+1,N):
                Difference = abs(a[i] - a[j])
                if Difference > self.maximumDifference:
                    self.maximumDifference = Difference
        
        # Loop above written in this way to ensure we are not looping back over the same elements
        
# ------------------------------------ End Solution ---------------------------------------------------------------
 
# ---------------------------- HackerRank provided code and input below -------------------------------------------

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
