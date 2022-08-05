n = int(input("Enter the number of process: "))
print("Enter the process id and burst time respectively: ")

process_list = []

for i in range(n):
    process_list.append(list(map(int, input().split()))) # list = [3, 6]   process_list[[1,4], [2,5],[3, 6] ]

for i in range(n):
    for j in range(i + 1, n):
        if process_list[i][1] > process_list[j][1]:
            process_list[i], process_list[j] = process_list[j], process_list[i]

completation_time = 0

for i in range(n):
    completation_time += process_list[i][1]    #ct = 4
    process_list[i].append(completation_time)   #process_list[[1,4,4], []]

print("pid BT CT/TAT WT")

turn_around_time, waiting_time = 0, 0

for i in range(n):
    print(process_list[i][0], " ", process_list[i][1], " ", process_list[i][2], " ", process_list[i][2] - process_list[i][1])
    turn_around_time += process_list[i][2]
    waiting_time += process_list[i][2] - process_list[i][1]

print("Average total burst time is: ", turn_around_time / n)
print("Average total waiting time is: ", waiting_time/n)
