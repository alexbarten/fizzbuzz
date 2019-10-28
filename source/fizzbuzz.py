"""
Write a short program that prints each number from 1 to 100 on a new line. 
For each multiple of 3, print "Fizz" instead of the number. 
For each multiple of 5, print "Buzz" instead of the number. 
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of 
the number.

This version is easy to test, and has a clear separation of concerns.
"""

def fizzbuzz(i):
    output = ''
    if i % 3 == 0: output = 'Fizz'
    if i % 5 == 0: output += 'Buzz'
    return(output or i)

if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
