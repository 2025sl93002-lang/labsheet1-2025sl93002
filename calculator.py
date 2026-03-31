def add(a, b):
<<<<<<< HEAD
    return a + b
=======
    return a + b   
>>>>>>> c1cbbe36711d3dff92b16292174a8670ddd7a828

def multiply(a, b):
    return a * b

<<<<<<< HEAD
def divide(a, b):
    return a / b
=======
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
>>>>>>> c1cbbe36711d3dff92b16292174a8670ddd7a828
