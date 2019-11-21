#!/usr/bin/env python3

import locale

# set the locale for use in currency formatting
result = locale.setlocale(locale.LC_ALL, '')
if result == 'C':
    locale.setlocale(locale.LC_ALL, 'en_US')

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    monthly_investment = float(input("Enter monthly investment:\t"))
    while monthly_investment <= 0:
        print("Entry must be greater than 0. please try again.") 
        monthly_investment = float(input("Enter monthly investment:\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    while yearly_interest_rate <= 0 or yearly_interest_rate >= 16:
        print("Entry must be greater then 0 and less than or equal to 15. Please try again.")
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    year = int(input("Enter number of years:\t\t"))
    while year <= 0 or year > 50:
        print("Years must be greater than 0 and less then or equal to 51. please try again.")
        year = int(input("Enter number of years:\t\t"))
       

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = year * 12

    # calculate the future value
    future_value = 0
    for i in range (1, months + 1):
        future_value = future_value + monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value = future_value + monthly_interest_amount
        if i % 12 == 0:
            print("Year = ", i // 12 , "Future Value =" , round(future_value, 2))

    # format and display the result
    print()
    print()

    # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")
