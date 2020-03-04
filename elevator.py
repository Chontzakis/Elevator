import random
import time

class Person:
    def __init__(self,id,start,end,inlift = False):
        self.id = id
        self.start = start
        self.end = end
        self.inlift = inlift
    def get_in(self, lift):
        if self.start == lift.floor and self.inlift == False :
            self.inlift = True
    def get_out(self,lift):
        if self.end == lift.floor and self.inlift == True :
            self.inlift = False
    def __str__(self):
        return str(self.id)
    def setin(self,y):
        self.inlift = y
    def gin(self):
        return self.inlift
class Lift:
    def __init__(self, floors, floor = -1, move = 1):
        self.floors = floors
        self.floor = floor
        self.move = move
    def start(self):
        self.floor += self.move
    def setmove(self,y):
        self.move = y
    def getmove(self):
        return self.move
    def detfloor(self,y):
        self.floor = y

class Building:
    def __init__(self,floors,passengers,lift):
        self.floors = floors
        self.passengers = passengers
        self.lift = lift
    def run(self):
        self.lift.start()

    def graphics(self, Floors, Passengers, lift):
        self.lift = lift
        print('Floors    Passengers    Lift')
        for i in Floors:
            view = []
            for a in Passengers[i]:
                view.append(str(a))
            if i == lift.floor:
                print(i, '\t', '  ', ','.join(view), ' ' * (13 - 2 * len(view) - 1), '#')
            else:
                print(i, '\t', '  ', ','.join(view))
    def createfloors(self,floors):
        Floors = []  # 5,4,3,2,1
        for i in range(floors):
            Floors.append(floors - i)
        Floors.append(0)  # Floors = [5,4,3,2,1,0]
        return Floors
    def createpeople(self,passengers,floors):
        people = []
        for i in range(1, passengers + 1):
            start = random.randint(1, floors)
            stop = random.randint(1, floors)
            while start == stop:
                start = random.randint(1, floors)
                stop = random.randint(1, floors)
            people.append(Person(i, start, stop))  # people = [[main<1>],[main<2>]]
        Passengers = list('_' * (floors + 1))       #Sorting people in their starting floors
        for i in range(len(Passengers)):
            Passengers[i] = []  # [[],[],[],[],[],[]]
        for i in range(floors + 1):
            for person in people:
                if person.start == i:
                    Passengers[i].append(person)  # Passengers = [[],[<__main__.Person object at 0x1066732b0>]]
        return people,Passengers
    def inn(self,i,people,Passengers):
        time.sleep(delay)
        print('\n'*100)
        self.run()
        for person in  people :
            if person.start == i :
                Passengers[i].remove(person)
                person.setin(True)
        return Passengers
    def out(self,i,people,Passengers,lift):
        self.lift = lift
        time.sleep(delay)
        print('\n' * 100)
        for person in people:
            if person.end == self.lift.floor:
                Passengers[lift.floor].append(person)
                person.setin(False)
        return Passengers
try:
    floors = int(input('Give me the number of floors: '))
except ValueError:
    print('Please give me integer')
    floors = int(input('Give me the number of floors: '))
try :
    passengers = int(input('Give me the number of passengers: '))
except ValueError:
    print('Please give me integer')
    passengers = int(input('Give me the number of passengers: '))
try :
    delay = int(input('Give me the delay time: '))
except ValueError :
    print('Please give me integer')
    delay = int(input('Give me the delay time: '))

def main(floors,passengers) :
    lift = Lift(floors)
    building = Building(floors,passengers,lift)
    Floors = building.createfloors(floors)
    people , Passengers = building.createpeople(passengers,floors)
    for i in range(floors+1):       #i = lift.floor     #Lift going up
        Passengers = building.inn(i,people,Passengers)
        building.graphics(Floors,Passengers,lift)
    lift.setmove(-1)
    for person in people:
        if person.end == floors and person.gin == True :
            Passengers[floors].append(person)
    for i in range(floors+1):           #Lift going down
        Passengers = building.out(i,people,Passengers,lift)
        building.graphics(Floors,Passengers,lift)
        building.run()

main(floors,passengers)




