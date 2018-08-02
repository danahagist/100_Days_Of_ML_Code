# --------- Objective and Instructions----------
# Today, we're delving into Inheritance. 

# Task
# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
# Completed code for Person and a declaration for Student are provided for you in the editor. 
# Observe that Student inherits all the properties of Person.

# Complete the Student class by writing the following:

# *** A Student class constructor, which has parameters:
# 1. A string, firstName.
# 2. A string, lastName.
# 3. An integer, id.
# 4. An integer array (or vector) of test scores, scores. 

# *** A char calculate() method that calculates a Student object's average 
# and returns the grade character representative of their calculated average:

# HackerRank provided the following code for the Person class:
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)  
   
# ---------- Solution----------
# Creating Student subclass of Person class
class Student(Person):
    # initializing Student subclass
    def __init__(self, firstName, lastName, idNumber, scores):
            # Inheriting Person properties
            Person.__init__(self, firstName, lastName, idNumber)
            # Assigning scores (an input) to self.scores
            self.scores =scores
    
    # Creating method for grade calculation, per instructions
    def calculate(self):
        avg_score = sum(self.scores)/len(self.scores)
        if avg_score < 40:
            return "T"
        elif 40 <= avg_score < 55:
            return "D"
        elif 55 <= avg_score < 70:
            return "P"
        elif 70 <= avg_score < 80:
            return "A"
        elif 80 <= avg_score < 90:
            return "E"
        elif 90 <= avg_score <= 100:
            return "O"
        else:
            return ""
    
# --------- End Solution ----------
    
# HackerRank provided following for solution validation:
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())
