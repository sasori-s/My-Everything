input_string = input("Enter a sentence: ")
input_letter = input("Enter a letter: ")

if input_letter in input_string:
    output = input_string.replace(input_letter, "")
    print(output)

else:
    input_string = input_string[1:-2]
    print(input_string)

