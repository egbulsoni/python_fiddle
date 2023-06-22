# Ask user for their name
name = input("What's your name?")

# remove whitespace
name = name.strip().title()

# split user's name into first name and last name
first, last = name.split(" ")
# capitalize user's name
# name = name.capitalize()

# Capitalize user's name
# name = name.title()

# say hello to user
# print("hello, " + name)
# adds space before second parameter
# print("hello,", name)

print(f"hello, {first}")
