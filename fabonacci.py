def fibonacci(n):
    """
    Function to generate Fibonacci sequence up to n terms.
    """
    sequence = []
    
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence


# User input
terms = int(input("Enter number of terms: "))
print("Fibonacci sequence:", fibonacci(terms))
