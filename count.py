# Count Notes Program

amount = int(input("Enter amount: "))

notes = [1000, 500, 100, 50, 20, 10, 5, 1]

print("\nNumber of notes:")

for note in notes:
    count = amount // note
    if count > 0:
        print(note, "notes:", count)

    amount = amount % note