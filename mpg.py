#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
choice = "y"
while choice.lower() == "y":
    miles_driven= float(input("Enter miles driven:\t\t"))
    gallons_used = float(input("Enter gallons of gas used:\t"))
    gallon_cost = float(input("Enter cost per gallon:\t\t"))
    # calculate miles per gallon

    mpg = miles_driven / gallons_used
    mpg = round(mpg, 1)
    cpg = gallons_used / gallon_cost
    cpg = round(cpg, 1)
    tgc = gallon_cost * gallons_used
    tgc = round(tgc, 1)
    cpm = tgc / miles_driven
    cpm = round(cpm, 1)
        
    # format and display the result
    print()
    print("Miles Per Gallon:", mpg)
    print("Total gas cost:\t", tgc)
    print("Cost Per Mile:\t", cpm)
    choice = input("Get entries for another trip (y/n)?:")
    print()
print("Bye")

