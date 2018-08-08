# Task:
# To solve this challenge, we must first take each character in s, enqueue it in a queue, 
# and also push that same character onto a stack. 
# Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, 
# then compare the two characters to see if they are the same;  
# as long as the characters match, we continue dequeueing, popping, 
# and comparing each character until our containers are empty (a non-match means s isn't a palindrome).

# Write the following declarations and implementations:

#    1. Two instance variables: one for your stack, and one for your queue.
#    2. A void pushCharacter(char ch) method that pushes a character onto a stack.
#    3. A void enqueueCharacter(char ch) method that enqueues a character in the queue instance variable.
#    4. A char popCharacter() method that pops and returns the character at the top of the stack instance variable.
#    5. A char dequeueCharacter() method that dequeues and returns the first character in the queue instance variable.

# ----------------------------------------------- Solution ----------------------------------------------------------
import sys

class Solution:
    # Initializing with stack and queue attributes
    def __init__(self):
        self.stack = []
        self.queue = []
    # Pushing character onto stack, adding to end ("right side")
    def pushCharacter(self, ch):
        self.stack.append(ch)
    # Popping character from stack, removing from end ("right side")
    def popCharacter(self):
        return self.stack.pop()
    # Enqueueing character to queue, adding to beginning ("left side")
    def enqueueCharacter(self, ch):
        self.queue.insert(0,ch)
    # Dequeueing character from queue, removing from end ("right side")
    def dequeueCharacter(self):
        return self.queue.pop()

# -------------------------------------------- End Solution -------------------------------------------------------

# ------------------------------------------- HackerRank Input ----------------------------------------------------

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")   
    
# ------------------------------------------------- End File -------------------------------------------------------    
