class student:
  def init(self, Name, ID):
    self.name = Name
    self.id = ID

class seat:
  def init(self, Name):
    self.no = Name
    self.ownby = None

  def add_holder(self, std):
    self.ownby = std

class hall:
  def init(self):
    self.seats = list()

  def add_seat(self, seat_no):
    self.seats.append(seat(seat_no))

  def add_student(self, std):
    for i in self.seats:
      if i.ownby == None:
        i.add_holder(std)
        print(i.no + " is booked by " + i.ownby.id)
        break

  def print_seats(self):
    for i in self.seats:
      print(i.no)
      if i.ownby == None:
        print("seat is free")
      else:
        print(i.ownby.name, i.ownby.id)

yksg = hall()
yksg.add_seat("501A")
yksg.add_seat("501B")
yksg.add_seat("501C")
yksg.add_seat("501D")
yksg.add_seat("502A")
yksg.add_seat("502B")
yksg.add_seat("502C")
yksg.add_seat("502D")
yksg.add_seat("503A")
yksg.add_seat("503B")
yksg.add_seat("504A")
yksg.add_seat("504B")
yksg.add_seat("504C")
yksg.add_seat("504D")

for i in range(15):
  std_name = input("Enter Student Name: ")
  std_id = input("Enter Student ID: ")
  yksg.add_student(student(std_name, std_id))