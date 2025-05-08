# Define the factorial function using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function with a sample number
number = int(input("Enter a number: "))
print(f"Factorial of {number} is: {factorial(number)}")
