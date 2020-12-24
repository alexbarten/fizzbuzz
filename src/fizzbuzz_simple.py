"""
Write a short program that prints each number from 1 to 100 on a new line. 
For each multiple of 3, print "Fizz" instead of the number. 
For each multiple of 5, print "Buzz" instead of the number. 
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of
the number.

This solution is a basic interpretation of the solution. No separation of 
concerns, just the bare minimum.
"""

def fizzbuzz():
    for i in range(1, 101):
        output = ''
        if i % 3 == 0: output = 'Fizz'
        if i % 5 == 0: output += 'Buzz'
        print(output or i)
        # print(i if output == '' else output) - alternative solution
        
fizzbuzz()
