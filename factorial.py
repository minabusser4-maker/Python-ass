def factorial(n):
    """
    Function to compute factorial of a number.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


# User input
num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))



