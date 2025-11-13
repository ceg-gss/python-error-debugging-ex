# fixed_division.py

def divide(a, b):
    """Safely divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    x = 10
    y = 0  # still zero, but now we handle it cleanly
    try:
        print("Result:", divide(x, y))
    except ValueError as e:
        print("Error:", e)
