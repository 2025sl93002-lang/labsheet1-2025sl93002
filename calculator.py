def add(a, b):
    return a + b   

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return None
    return a / b


# ---------------- TEST CASES ----------------

print("Running test cases...")

# this should be 15, but add() is wrong → pipeline will fail
assert add(10, 5) == 15

print("All tests passed")
