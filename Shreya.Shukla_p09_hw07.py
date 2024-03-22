# -*- coding: utf-8 -*-
#Shreya  Shukla
#IntroCS2 pd10
#HW07 -- <Title/Topic/Summary>
#2019--02--25

# takes numeric inputs a, b, c -- representing side lengths of a triangle -- and returns a boolean value to
#indicate whether the they constitute a Pythagorean triple.

(a, b, c) = input ("PythTriple")

PythTriple = False

if a == b == c == 0:
    print ("Please enter valid numbers.")
elif ((a ** 2) + (b**2)) == (c ** 2):
    PythTriple = True
    
print (PythTriple)

###TestCases
#pythTriple(0,0,0) → False
#pythTriple(3,4,5) → True
#pythTriple(3,4,6) → False


# takes a numeric input g, representing a student’s grade, and returns its letter grade equivalent
g = input ("gradeConv:" )

if g <= 100:
    if g  >=  90  :
        print ("A")
if g < 90:
    if g  >=  80 :
        print ("B")
if g < 80:
    if g >= 70 :
        print ("C")
if g <= 69:
    if g >= 65 :
        print ("D")

if g <= 64:
    if g >= 0 :
        print ("F")

if g > 100 or g < 0:
    print ("Please enter a number between 0 and 100")
    
###TestCases
#gradeConv 100 --> A
#gradeConv 90 --> A
#gradeConv 89 --> B
#gradeConv 79 --> C
#gradeConv 69 --> D
#gradeConv 65 --> D
#gradeConv 50 --> F
#gradecConv 0 --> F
#gradeConv 101 --> "Please enter a number between 0 and 100"
#gradeConv -1 --> "Please enter a number between 0 and 100"

    
#  takes a string input letterGrade and prints congratulatory or scolding messages.

letterGrade = str (input ("passJudgement:")) #enter a letter grade in quotes

if letterGrade == "A" :
    print ("Outstanding! You aced this, champ!")
elif letterGrade == "B":
    print ("Satisfactory, but you could do better. Spend more time into this!")
elif letterGrade == "C":
    print ("Barely satisfactory. You need to get AIS tutoring and speak to your teacher.")
elif letterGrade == "D":
    print ("Barely passing. Speak to me after class so I can help you do better.")
elif letterGrade == "F":
    print ("You FAILED the test! Did you study at all? Speak to me in room 403.")
else:
    print ("Please enter a letter grade from A-F.")
