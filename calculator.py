def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

if __name__ == "__main__":
    # Example usage
    print("Addition examples:")
    print(f"  5 + 3 = {add(5, 3)}")
    print(f"  10 + 20 = {add(10, 20)}")

    print("\nMultiplication examples:")
    print(f"  4 * 3 = {multiply(4, 3)}")
    print(f"  7 * 6 = {multiply(7, 6)}")