def fizz_buzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0 and num % 5 > 0):
        return "Fizz"
    elif (num % 5 == 0 and num % 3 > 0):
        return "Buzz"
    return num


num = int(input("Enter a Number: "))
print(fizz_buzz(num))
