import random
import numpy as np
class City:
    def __init__(self,x=None,y=None):
        if [x,y] != [None,None]:
            self.x=x
            self.y=y
        else:
            self.x=int(random.random() * 200)
            self.y=int(random.random() * 200)
    
    def distance(self,to):
        x=self.x-to.x
        y=self.y-to.y
        r=np.sqrt(x**2 + y**2)
        return r

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Fitness:
    def __init__(self,route):
        self.route=route
        self.distance=0.0
        self.fitness=0.0

    def routeDistance(self):
        total=0
        for i in range(len(self.route)):
            c1=self.route[int(i%len(self.route))]
            c2=self.route[int((i+1)%len(self.route))]
            total+=c1.distance(c2)
        
        self.distance=total
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = float(self.routeDistance())
        return self.fitness


def generateCities(ncity):
    cityList=[]
    for _ in range(ncity):
        cityList.append(City())
    return cityList

def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route

cityList=generateCities(50)
print(Fitness(createRoute(cityList)).routeFitness())
print(Fitness(createRoute(cityList)).routeFitness())
print(Fitness(createRoute(cityList)).routeFitness())
print(Fitness(createRoute(cityList)).routeFitness())
print(Fitness(createRoute(cityList)).routeFitness())
print(Fitness(createRoute(cityList)).routeFitness())
print(Fitness(createRoute(cityList)).routeFitness())

