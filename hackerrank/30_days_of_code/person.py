class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores=[]):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores 

    def calculate(self):
        s = sum(self.scores)/len(self.scores)
        if 90 <= s <= 100:
            return "O"
        elif 80 <= s < 90:
            return "E"
        elif 70 <= s < 80:
            return "A"
        elif 55 <= s < 70:
            return "P"
        elif 40 <= s <= 55:
            return "D"
        else:
            return "T"




p = Person("Jeff", "Reiher", 1)
p.printPerson()
scores = [80,100]
s = Student("Jack","Meoff", 2, scores)

# s.scores.append(80)
# s.scores.append(100)
# print s.scores
# print s.firstName
print s.printPerson()
print s.calculate()
