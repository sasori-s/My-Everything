def find_median(number_list, n, m):
    number_list.sort()
    median = number_list[2]
    average = sum(number_list)/5
    average = '{0:.3g}'.format(average)

    # print(median)
    # print(number_list)

    print(f"Hi {name} ({banner_number}), based on the input given:"
          f"\nfor {n}/{m} scores Tests = {number_list[0]}% PoDs = {number_list[1]}%, Assignments = {number_list[2]}"
          f"\nPracticum = {number_list[3]}%, Labs = {number_list[4]}%, "
          f"\nyour final score is {average}%"
          f"\nwith median {median}%")




print("Enter your name, Banner number and marks accordingly")
name = input()
banner_number = input()
m = int(input("Total number of assessment: "))
n = int(input("specify the amount of number you want to enter:  "))
number_list = []
for i in range(n):
    num = int(input())
    number_list.append(num)

for i in range(n, m):
    number_list.append(100)

find_median(number_list, n, m)