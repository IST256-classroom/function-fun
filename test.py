def generate_blanks(string1):
    num_blanks = '_' * len(string1)
    return num_blanks

user_input = input("Enter text: ")
print(generate_blanks(user_input))
