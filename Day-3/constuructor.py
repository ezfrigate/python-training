from math import pi
import numpy
import statistics

class Car():
    def __init__(self, num, c):
        self.num = num # self.num is an object variable 
        self.c = c

    def tyres(self):
        print("i have", self.num, "tyres")

    def color(self):
        print("my color is ", self.c, "and i have", self.num, "tyres")

obj = Car(4, "RED")
obj.tyres()
obj.color()

'''
create class circle in which take input radius in constructor
and in area method find area and in perimeter method find perimeter of circle

create class list_manipulation, in which take input elements of a list one by one
till user enters -999
in find_outlier method find the outlier in that list. use any of the methods 
3 Standard Deviation  technique (3 SD) or Inter Quartile Range (IQR) method
'''

class Circle():
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return self.rad**2*pi
    
    def perimeter(self):
        return self.rad*2*pi
    
obj = Circle(3)
print(obj.area())
print(obj.perimeter())

class list_manipulation():
    '''
    def __init__(self):
        STOP = -999
        self.lst = list(iter(input, int(STOP)))
    '''
    def __init__(self):
        user_input = 0
        self.list=[]
        list.__iter__
        while(int(user_input) != -999):
            user_input = input("enter a number to be entered in the list \n")
            if(int(user_input) != -999):
                self.list.append(int(user_input))
    
    def find_outlier(self):
        #elements = numpy.array(self.list)
        #sd = numpy.std(elements, axis=0)
        #mean = numpy.mean(elements, axis=0)
        sd = statistics.stdev(self.list)
        mean = statistics.mean(self.list)
        ans_list = [c for c in self.list if (c - mean) > 3*sd]
        return ans_list

obj = list_manipulation()
print(obj.find_outlier())