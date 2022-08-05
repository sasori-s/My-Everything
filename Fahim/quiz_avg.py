def calc_mark(string_list):
    total = 0
    marks = string_list.pop()
    marks = marks.replace(" ", "")
    print(marks)

    marks = marks.split(",")
    length = len(marks)
    marks = marks.sort(reverse= True)

    if length >= 3:
       for i in range(length - 1):
          total = total + marks[i]
          avg = total/ length - 1
          print(avg)

    else:
        for i in range(length-2):
            total = total + marks[i]
            avg = total/length- 2
            print(avg)

string_list = ['7, 8,   9,    3']
calc_mark(string_list)