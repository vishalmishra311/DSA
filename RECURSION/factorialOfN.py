# factorial of N using recurision .

def factorial(number):
    if (number == 1):
        return 1
    factorialAnswer = number * factorial(number - 1)
    return(factorialAnswer)
userInput = int(input("enter number==>"))
print(factorial(userInput))