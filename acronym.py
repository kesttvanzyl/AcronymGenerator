#! /usr/bin/python
# Exercise No.   1
# File Name:     acronym.py
# Programmers:    Kestt van Zyl
# Date:          September 27, 2020
#
# A program that allows the user to type in a phrase and then outputs the acronym for that phrase.
#
# Problem Statement: Write a program that allows user to type in a phrase and then outputs the acronym for that phrase.
#
# Overall Plan:
# 1. Print Description Message
# 2. Prompt user to enter phrase and assign input to the variable "user_phrase
# 3. split the phrase into substrings and assign assign the substrings to the variable "user_phrase_separated"
# 4. create blank string
# 5. create for loop with if statement inside to exclude "and" from the acronyms
# 6. store the capitalized first letter of each word into the variable "acronym"
# 7. print the results

def main():

    # Description Message
    print("This program turns a phrase that you enter into an acronym!")

    # Prompting the user to enter phrase
    user_phrase = input("Please enter a phrase: ")

    # Separating the phrase into substrings
    user_phrase_separated = user_phrase.split()

    # Blank string that we will add letters to in the loop
    acronym = ""

    # For loop
    for i in user_phrase_separated:
        # This line prevents the program from adding "and" into the acronym because "and" is traditionally excluded
        if i != "and" and "And" and "AND":
            # Capitalizes the first letter of each word and adds it to the blank string I created earlier
            acronym = acronym + i[0].upper()

    # Prints the results
    print("The acronym for the phrase that you entered is: " + acronym)


main()


