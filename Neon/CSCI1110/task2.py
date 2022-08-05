def find_median(number_list):
    number_list.sort()
    median = number_list[2]
    average = sum(number_list)/5
    average = '{0:.3g}'.format(average)

    # print(median)
    # print(number_list)

    print(f"Hi {name} ({banner_number}), based on the input given:"
          f"\nTests = {number_list[0]}% PoDs = {number_list[1]}%, Assignments = {number_list[2]}"
          f"\nPracticum = {number_list[3]}%, Labs = {number_list[4]}%, your final score is {average}%"
          f"\nwith median {median}%")


print("Enter your name, Banner number and marks accordingly")
name = input()
banner_number = input()

number_list = []
n = 5
for i in range(n):
    num = int(input())
    number_list.append(num)

find_median(number_list)