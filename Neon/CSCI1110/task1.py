print("Enter your name, Banner number and marks accordingly")
name = input()
banner_number = input()
tests = int(input())
PoD = int(input())
assignments = int(input())
practicum = int(input())
labs = int(input())

average = 0.0
average = (tests + PoD + assignments + practicum + labs)/5

print(f"Hi {name} ({banner_number}), based on the input given:"
      f"\nTests = {tests}% PoDs = {PoD}%, Assignments = {assignments}"
      f"\nPracticum = {practicum}%, Labs = {labs}%, your final score is {average}%")
