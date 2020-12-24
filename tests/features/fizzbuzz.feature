Feature: Solve the FizzBuzz problem
As a programmer,
I want to solve the FizzBuzz programming problem,
so that I can show off my basic Python skills.

Scenario: Print Fizz for multiples of 3
    Given that we go through a loop from 1 until 100
    When the number is a multiple of 3
    Then the program prints "Fizz" instead of the number

Scenario: Print Buzz for multiples of 5
    Given that we go through a loop from 1 until 100
    When the number is a multiple of 5
    Then the program prints "Buzz" instead of the number

Scenario: Print FizzBuzz for multiples of 5 and 3
    Given that we go through a loop from 1 until 100
    When the number is a multiple of 5
    And the number is a multiple of 3
    Then the program prints "FizzBuzz" instead of the number

Scenario: Print the number for non-multiples
    Given that we go through a loop from 1 until 100
    When the number is not a multiple of 5
    And the number is not a multiple of 3
    Then the program prints the number
