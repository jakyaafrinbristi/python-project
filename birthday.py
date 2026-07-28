# Storing Birthdays Project

birthdays = {}

while True:
    print("\n--- Birthday Storage System ---")
    print("1. Add Birthday")
    print("2. View All Birthdays")
    print("3. Search Birthday")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter person's name: ")
        birthday = input("Enter birthday (DD-MM-YYYY): ")

        birthdays[name] = birthday
        print("Birthday saved successfully!")

    elif choice == "2":
        if birthdays:
            print("\nStored Birthdays:")
            for name, date in birthdays.items():
                print(name, ":", date)
        else:
            print("No birthdays stored.")

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in birthdays:
            print(name, "birthday is", birthdays[name])
        else:
            print("Birthday not found.")

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")