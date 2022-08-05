user_input = int(input("Enter a number: "))
sum = 0
counter = 1

while (counter * 7) <= user_input:
    sum = sum + (counter * 7)
    counter = counter + 1

print(sum)