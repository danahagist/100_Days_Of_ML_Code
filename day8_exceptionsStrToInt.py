## Task:
# Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

# Note: You must use the String-to-Integer and exception handling constructs built into your submission language. 
# If you attempt to use loops/conditional statements, you will get a 0 score.

# ----------------------------- Dataquest creates 'S' as input variable -----------------------------------------

S = input().strip()

# -------------------------------------------- Solution ---------------------------------------------------------

# This was the most simple solution that came to mind, and doesn't seem inefficient or difficult to understand.

# Using try block for first 2 lines of code
try:
    # int(S) converts S to int and then print... prints.
    print(int(S))
# Exception block
except:
    # printing exception string when int(S) cannot be converted
    print('Bad String')
    
# ------------------------------------------ End Solution ---------------------------------------------------------

# ------------------------------------------- End File ------------------------------------------------------------
