# String Operations Project

text = input("Enter a string: ")

print("\nOriginal String:", text)

# String Length
print("Length of string:", len(text))

# Uppercase
print("Uppercase:", text.upper())

# Lowercase
print("Lowercase:", text.lower())

# Reverse String
print("Reverse:", text[::-1])

# Count a character
character = input("Enter a character to count: ")
print("Character count:", text.count(character))

# Replace a word
old = input("Enter word to replace: ")
new = input("Enter new word: ")

print("After Replace:", text.replace(old, new))