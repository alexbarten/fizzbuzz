from pytest_bdd import scenario, given, when, then

scenario('fizzbuzz.feature', 'Print Fizz for multiples of 3')
def test_fizzbuzz():
    pass

@given('that we go through a loop from 1 until 100')
def loop_till_hundred():
    pass

@when('the number is a multiple of 3')
def multiple_of_three():
    pass

@then('print "Fizz" instead of the number')
def print_fizz():
    pass
