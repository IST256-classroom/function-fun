def check_character_in_word(str_1, str_2):
    for c in str_2:
        if c == str_1:
            return 'True'
        elif c != str_1:
            return 'False'

str_1 = input("Enter a character: ")
str_2 = input("Enter some text: ")
y = check_character_in_word(str_1, str_2)
print(y)
