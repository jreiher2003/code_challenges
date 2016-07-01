from operator import itemgetter
from itertools import groupby

directory = [["Mike Thomson", 20, "M"],["Robert Bustle", 32, "M"],["Andria Bustle", 30, "F"]]
directory.sort(key=itemgetter(1))
for i,name in groupby(directory, itemgetter(1)):
    for x in name:
        if x[2] == "M":
            print "Mr. " + x[0]
        if x[2] == "F":
            print "Ms. " + x[0]


def peopleformat(func):
    def peopletoformat(peoples):
        for i in range(len(peoples)):
            temp = peoples[i].strip().split()
            if temp[-1] == 'M':
                flag = 'Mr. '
            else:
                flag = 'Ms. '
            peoples[i] = [flag + ' '.join(temp[:-2]), int(temp[-2])]
        return func(peoples)
    return peopletoformat
    
@peopleformat
def peoplesort(peoples):
    for x, y in sorted(peoples, key=lambda x: x[1]):
        print x
    