#!/usr/bin/env python
# HW02_ex05_02

# Write a function called do_n that takes a function object and a number, n, as 
# arguments, and that calls the given function n times.

################################################################################
# Write your functions below:

def print_lyrics():
	print 'hour follows hour'
	print 'like water follows water'

def do_n(o, n):
	if n <= 0:
		return
	print_lyrics()
	do_n(o, n - 1)


# Write your functions above:
def print_hello():
    print("Hello World")
################################################################################
def main():
    do_n(print_lyrics, 4)
    
  



if __name__ == "__main__":
    main()