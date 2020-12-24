def fizzbuzz(number):
    result = ''
    if number % 3 == 0: result = "Fizz"
    if number % 5 == 0: result += "Buzz"
    return result or number

def output(fizzbuzz_result):
    print(fizzbuzz_result)

def main():
    for i in range(1, 101):
        output(fizzbuzz(i))

if __name__ == "__main__":
    main()
