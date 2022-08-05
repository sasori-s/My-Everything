if __name__ == '__main__':

    total_process_no = int(input("Enter Total Process Number: "))
    total_time = 0
    total_time_counted = 0

    processes = []
    waiting_time = 0
    turnaround_time = 0


    for x in range(total_process_no):

        print("Enter process arrival time and burst time")
        input_info = list(map(int, input().split(" ")))
        arrival, burst, remaining_time = input_info[0], input_info[1], input_info[1]

        processes.append([arrival, burst, remaining_time, 0])

        total_time += burst
    print("Enter time quantum")
    time_quantum = int(input())

    while total_time != 0:

        for i in range(len(processes)):

            if processes[i][2] <= time_quantum and processes[i][2] >= 0:
                total_time_counted += processes[i][2]
                total_time -= processes[i][2]

                processes[i][2] = 0
            elif processes[i][2] > 0:

                processes[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
            if processes[i][2] == 0 and processes[i][3] != 1:


                waiting_time += total_time_counted - processes[i][0] - processes[i][1]
                turnaround_time += total_time_counted - processes[i][0]

                processes[i][3] = 1
    print("\nAvg Waiting Time is ", (waiting_time * 1) / total_process_no)
    print("Avg Turnaround Time is ", (turnaround_time * 1) / total_process_no)