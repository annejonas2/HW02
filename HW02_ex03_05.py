#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.


# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

#1

def two_by_two():
    print '+', (' - ' * 4), '+', (' - ' * 4), '+'
    print '|', (' ' * 12), '|', (' ' * 12), '|'
    print '|', (' ' * 12), '|', (' ' * 12), '|'
    print '|', (' ' * 12), '|', (' ' * 12), '|'
    print '|', (' ' * 12), '|', (' ' * 12), '|' 
    print '+', (' - ' * 4), '+', (' - ' * 4), '+'
    print '|', (' ' * 12), '|', (' ' * 12), '|'
    print '|', (' ' * 12), '|', (' ' * 12), '|'
    print '|', (' ' * 12), '|', (' ' * 12), '|'
    print '|', (' ' * 12), '|', (' ' * 12), '|' 
    print '+', (' - ' * 4), '+', (' - ' * 4), '+'

#2

def do_twice(f,k):
    f(k)
    f(k)

def print_twice(k):
    print k
    print k

mid_line = ('| ') + (' ' * 12) + (' | ') + (' ' * 12) + (' |' )

big_mid_line = mid_line +  (' ' * 12) + (' | ') + (' ' * 12) + (' |' )

plus_line = ('+ ') + (' - ' * 4) + (' + ') + (' - ' * 4) + ' +'

big_plus_line = plus_line + (' - ' * 4) + (' + ') + (' - ' * 4) + ' +'


def four_by_four():
	print big_plus_line
	do_twice(print_twice , big_mid_line)
	print big_plus_line
	do_twice(print_twice , big_mid_line)
	print big_plus_line
	do_twice(print_twice , big_mid_line)
	print big_plus_line
	do_twice(print_twice , big_mid_line)
	print big_plus_line
	
	

	

# Write your functions above:
################################################################################
def main():
    two_by_two()
    four_by_four()
    print("Hello World!")
    


if __name__ == "__main__":
    main()