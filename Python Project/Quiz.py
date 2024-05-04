# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:02:40 2024

@author: vaibhav
"""

score = 0

print("\t\t\t\t'Welcome to the Quiz'\n")

Name = input("Please Enter your name: ")

print("Hello",Name,"Please Enter `a,b,c or d` as your answer for the following questions: \n")

# Question 1
Answer1 = input("1. What does the len() function in Python do? \n a. Returns the length of a string. \n b. Returns the number of elements in a list. \n c. Returns the number of characters in a file. \n d. Returns the number of elements in a dictionary. \nAnswer: ")

if Answer1 == "b" or Answer1 == "B":
    score = score + 1
    print("Correct  Answer.")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect Answer.")
    print("The  correct answer is Option 'B'.")
    print("Score: ", score)
    print("\n")
    
# Question 2
Answer2 = input("2. Which of the following is not a valid variable name in Python? \n a. my_var \n b. _var \n c. 3var \n d. var_3 \nAnswer: ")

if Answer2 == "c" or Answer2 == "C":
    score = score + 1
    print("Correct  Answer.")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect Answer.")
    print("The  correct answer is Option 'C'.")
    print("Score: ", score)
    print("\n")
    
# Question 3
Answer3 = input("3. Which keyword is used to define a function in Python?\n a. func \n b. def \n c. define \n d. function \nAnswer: ")

if Answer3 == "b" or Answer3 == "B":
    score = score + 1
    print("Correct  Answer.")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect Answer.")
    print("The  correct answer is Option 'B'.")
    print("Score: ", score)
    print("\n")
 
# Question 4
Answer4 = input("4. How do you comment out code in Python?\n a. // \n b. -- \n c. * \n d. ''' \nAnswer: ")

if Answer4 == "d" or Answer4 == "D":
    score = score + 1
    print("Correct  Answer.")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect Answer.")
    print("The  correct answer is Option 'D'.")
    print("Score: ", score)
    print("\n") 

# Question 5
Answer5 = input("5. What method is used to add an item to the end of a list in Python?\n a. `append()` \n b. `insert()` \n c. `extend()` \n d. `add()` \nAnswer: ")

if Answer5 == "a" or Answer4 == "A":
    score = score + 1
    print("Correct  Answer.")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect Answer.")
    print("The  correct answer is Option 'A'.")
    print("Score: ", score)
    print("\n") 
    

#Goodbye Message
print("That concludes our quiz! Thank you for your participation.\n")

if score <= 2:
    print("Your final score is: ", score, "\nKeep practicing, you'll get there!")
elif score <= 4:
    print("Your final score is: ", score, "\nNice effort, keep it up!")
else:
    print("Your final score is: ", score, "\nWell done, you nailed it!")
    

