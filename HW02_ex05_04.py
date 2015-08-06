#!/usr/bin/env python
# HW02_ex05_04

# If you are given three sticks, you may or may not be able to arrange them in a 
# triangle. For example, if one of the sticks is 12 inches long and the other 
# two are one inch long, it is clear that you will not be able to get the short 
# sticks to meet in the middle. For any three lengths, there is a simple test to
# see if it is possible to form a triangle:

#   If any of the three lengths is greater than the sum of the other two, then 
#   you cannot form a triangle. Otherwise, you can. (If the sum of two lengths
#   equals the third, they form what is called a "degenerate" triangle.)

# (1) Write a function named is_triangle that takes three integers as arguments, 
# and that prints either "Yes" or "No," depending on whether you can or cannot 
# form a triangle from sticks with the given lengths.

# (2) Write a function that prompts the user to input three stick lengths, 
# converts them to integers, and uses is_triangle to check whether sticks with 
# the given lengths can form a triangle.

################################################################################
# Write your functions below:

def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print 'No'
    else:
        print 'Yes'

def check_stick_lengths():
    first_stick = raw_input('How long is the first stick?\n')
    second_stick = raw_input('How long is the second stick?\n')
    third_stick = raw_input('How long is the third stick?\n')
    is_triangle(int(first_stick), int(second_stick), int(third_stick))




# Write your functions above:
################################################################################
def main():

    is_triangle(1,2,3)
    is_triangle(1,2,4)
    is_triangle(1,5,3)
    is_triangle(6,2,3)
    
    check_stick_lengths()

    print("Hello World!")



if __name__ == "__main__":
    main()