# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:47:51 2024

@author: vaibhav
"""

import json

# Function to load questions from a JSON file
def load():
    # Open the JSON file containing the questions in read mode
    with open("questions.json", "r") as file:
        # Load the questions from the JSON file into a Python dictionary
        questions = json.load(file)
    # Return the loaded questions
    return questions

# Function to save questions to a JSON file
def save(questions):
    # Open the JSON file in write mode
    with open("questions.json", "w") as file:
        # Write the questions dictionary to the JSON file with indentation for readability
        json.dump(questions, file, indent=4)

# Function to display questions for a given level
def display(level, questions):
    print("---", level.capitalize(), "Level Questions ---")
    # Iterate over each question in the specified level
    for i, question in enumerate(questions[level], start=1):
        # Print the question number and text
        print("Question", i, ":", question['question'])
        # Iterate over each option for the question and print it
        for option in question['options']:
            print(option)
        # Print a blank line for space between questions
        print()

# Function to play the quiz
def play(questions, scores):
    # Ask for the player's name
    name = input("Enter your name: ")
    # Define the levels of difficulty
    levels = ["easy", "moderate", "hard"]
    # Initialize the player's scores if they are not already in the scores dictionary
    if name not in scores:
        scores[name] = {"easy": 0, "moderate": 0, "hard": 0}
    # Iterate over each level
    for level in levels:
        # Print a message indicating the player's current level
        print("\n", name + ",", "you are now in the", level, "level.")
        # Iterate over each question in the current level
        for question in questions[level]:
            # Print the question
            print(question['question'])
            print()
            # Print the options for the question
            for i, option in enumerate(question['options'], start=1):
                print(str(i) + ".", option)
            # Ask the player for their answer
            user_answer = input("Your answer: ")
            # Check if the answer is correct
            if user_answer.lower() == question['answer'].lower():
                print("Correct!")
                # Increment the player's score for the current level
                scores[name][level] += 1
            else:
                # If the answer is incorrect, print the correct answer
                print("Incorrect! The correct answer is:", question['answer'])
        # Print the player's score for the current level
        print("Your score for", level, "level:", scores[name][level], "/", len(questions[level]))
        # Check if there are more levels to play
        if level != levels[-1]:
            # Ask the player if they want to proceed to the next level
            next_level = input("Do you want to proceed to the next level? (yes/no): ").lower()
            # If the player doesn't want to proceed, end the game
            if next_level != "yes":
                print("Thank you for playing!")
                break

# Function to add a new question
def add(questions):
    level = input("Enter the level for the new question (easy/moderate/hard): ")
    new_question = input("Enter the question: ")
    options = [input("Enter option " + str(i + 1) + ": ") for i in range(4)]
    answer = input("Enter the correct answer: ")
    if level in questions:
        questions[level].append({"question": new_question, "options": options, "answer": answer})
        save(questions)
        print("Question added successfully!")
    else:
        print("Invalid level! Please enter easy, moderate, or hard.")


# Function to remove a question
def remove(questions):
    level = input("Enter the level of the question to remove (easy/moderate/hard): ").lower()
    question_index = int(input("Enter the index of the question to remove (1-" + str(len(questions[level])) + "): ")) - 1
    del questions[level][question_index]
    save(questions)
    print("Question removed successfully!")

# Function to check scores
def check(scores):
    print("\nScores:")
    for name, score_info in scores.items():
        print("Name:", name)
        for level, score in score_info.items():
            print(level.capitalize(), "Level:", score)
        print()  # Add an extra newline between each student's scores

# Function for authentication
def authenticate():
    password = input("Enter the password: ")
    if password == "Python":
        return True
    else:
        print("Incorrect password. Access denied.")
        return False

# Main function
def main():
    # Load questions from the JSON file
    questions = load()
    # Initialize an empty dictionary to store scores
    scores = {}

    while True:
        # Display the main menu options
        print("\nWelcome to the Quiz Game!")
        print("1. Play Quiz")
        print("2. Add Question (Teacher Only)")
        print("3. Remove Question (Teacher Only)")
        print("4. Check Scores (Teacher Only)")
        print("5. Exit")
        # Prompt the user to enter their choice
        choice = input("Enter your choice: ")

        # Execute the chosen option
        if choice == "1":
            # Play the quiz
            play(questions, scores)
        elif choice == "2":
            # If the user chooses to add a question, authenticate and then add
            if authenticate():
                add(questions)
        elif choice == "3":
            # If the user chooses to remove a question, authenticate and then remove
            if authenticate():
                remove(questions)
        elif choice == "4":
            # If the user chooses to check scores, authenticate and then display scores
            if authenticate():
                check(scores)
        elif choice == "5":
            # Exit the program if the user chooses to exit
            print("Thank you for playing!")
            break
        else:
            # Print an error message for invalid choices
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
