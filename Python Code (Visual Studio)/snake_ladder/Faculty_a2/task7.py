input_string = input("Enter a word: ")
number = int(input("Enter a input: "))

input_slice = input_string[ :number + 1]
input_reverse = input_slice[: : -1]

print(input_reverse)