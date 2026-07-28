# AND & OR Operator Program

age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ")

# AND Operator
if age >= 18 and has_id == "yes":
    print("You can enter.")

# OR Operator
elif age < 18 or has_id == "no":
    print("You cannot enter.")

else:
    print("Condition not matched.")