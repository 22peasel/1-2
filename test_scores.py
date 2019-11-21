#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
choice = "y"
while choice.lower() == "y":
      counter = 0
      total_score = 0       # initialize the variable for accumulating scores

      while True:
            score = input("Enter test score: ")
            if score == "end":
                  break
            score = int(score)
            if score >= 0 and score <= 100:
                  total_score += score # total_score = total_score + score
                  counter += 1 # elivia = elivia + 1
            else:
                  print("Test score must be from 0 through 100, Try again.")
      print(total_score, counter)
      # calculate average score
      average_score = round(total_score / counter)
                  
      # format and display the result
      print("======================")
      print("Total Score:  ", total_score, "\nAverage Score:", average_score)
      print()
      choice = input("Enter another set of test scores (y/n)? ")
print("Bye")


