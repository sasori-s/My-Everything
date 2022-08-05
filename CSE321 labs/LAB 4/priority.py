def findWaitingTime(process, n, waiting_time):
    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = process[i - 1][i] + waiting_time[i - 1]

def findTurnAroundTime(process, n, wt, turn_around_time):
    for i in range(n):
        turn_around_time[i] = process[i][1] + wt[i]

def findaverageTime(process, n):
    wt = [0] * n  #wt = [0, 0, 0]
    turn_around_time = [0] * n

    findWaitingTime(process, n, wt)
    findTurnAroundTime(process, n, wt, turn_around_time)

    print(" Process  Burst time  Waiting time  Turn-Around time")
    total_waiting_time = 0
    total_turn_around_time = 0

    for i in range(n):
        total_waiting_time = total_waiting_time + wt[i]
        total_turn_around_time = total_turn_around_time + turn_around_time[i]
        print(" ", process[i][0], " ", process[i][1], " ", wt[i], " ", turn_around_time[i])

    print("Average waiting time = %.5f" % (total_waiting_time / n))
    print("Average turn-Around time = ", total_turn_around_time)

def priorityScheduling(process, n):
    process = sorted(process, key = lambda proc:proc[2], reverse = True)

    print("Order in which process gets executed")
    for i in process:
        print(i[0])
    findaverageTime(process, n)


if __name__ == "__main__":
    proc = [[1, 24, 1],
            [2, 3, 0],
            [3, 3, 1]]

    n = 3
    priorityScheduling(proc, n)
