from pytest_bdd import given, when, then, scenario
from src.fizzbuzz_pythonic import fizzbuzz

 
@scenario('../features/fizzbuzz.feature', 'Print Fizz for multiples of 3')
def test_fizzbuzz():
    pass

@given('that we go through a loop from 1 until 100')
def loop_till_hundred():
    pass

@when('the number is a multiple of 3')
def multiple_of_three():
    assert fizzbuzz(3) == "Fizz"

@then('the program prints "Fizz" instead of the number')
def print_fizz():
    pass
