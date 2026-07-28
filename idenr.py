# Identity Operator Program

a = [1, 2, 3]
b = a
c = [1, 2, 3]

# Using is operator
if a is b:
    print("a and b are the same object")
else:
    print("a and b are different objects")

# Using is not operator
if a is not c:
    print("a and c are different objects")
else:
    print("a and c are the same object")