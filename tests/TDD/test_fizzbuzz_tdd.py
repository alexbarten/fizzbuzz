from src.fizzbuzz_tdd import fizzbuzz

# 1. Write a short program that prints each number from 1 to 100 on a new line.
# 2. For each multiple of 3, print "Fizz" instead of the number.
# 3. For each multiple of 5, print "Buzz" instead of the number.
# 4. For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

def test_min_max_in_1_to_100():
    result_list = []
    for i in range(1, 101):
        answer = fizzbuzz(i)
        if str(answer).isnumeric():
            result_list.append(answer)

    assert min(result_list) == 1
    assert max(result_list) == 98

def test_multiple_of_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(99) == "Fizz"

def test_multiple_of_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(95) == "Buzz"
    assert fizzbuzz(100) == "Buzz"

def test_multiple_of_3_and_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(90) == "FizzBuzz"
