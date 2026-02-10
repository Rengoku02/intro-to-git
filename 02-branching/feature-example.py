def add(x, y):
    """Add two numbers together."""
    return x + y


def multiply(x, y):
    """Multiply two numbers together."""
    return x * y


def calculate():
    """Run some example calculations."""
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")


if __name__ == "__main__":
    calculate()
