
# Task: 
# Given a base-10 integer, , convert it to binary (base-2). 
# Then, find and print the base-10 integer denoting the maximum number of consecutive '1s in n's binary representation.


# Takes input and assigns to n
n = int(input())

# Creating empty list to append our remainders to
# This will be a reversed representation of the binary number
rev_rep = []

# Looping through our n to convert to binary
while(n > 0):
    # Finding remainder of n modulus 2
    remainder = n % 2;
    # Using floor divide by 2
    n = n//2;
    # Appending remainder to my reverse representation
    rev_rep.append(remainder)

# Reversing order to get correct binary representation (bin_rep)
bin_rep = rev_rep[::-1]

# Loop to count consecutive 1's in bin
count_bin = 0
maximum = 0
for i in bin_rep:
    if i == 1:
        count_bin += 1
        if count_bin > maximum:
            maximum = count_bin
    else:
        count_bin = 0
   
# Printing maximum consecutive 1's 
print(maximum)
