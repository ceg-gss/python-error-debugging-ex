# buggy_division.py

def divide(a, b):
    # This will crash if b is zero
    return a / b

if __name__ == "__main__":
    x = 10
    y = 0  # intentional bug
    print("Result:", divide(x, y))
