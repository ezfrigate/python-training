'''
create a function to create list of marks of students. take marks
infinitely till user enters -ve marks
in calcualte function print

mean marks

standard deviation in marks

variance in marks

sum of all marks

median in marks

in another function sort marks in ascending order and print middle marks
there will be 2 middle marks if number of marks are even
there will be 1 middle marks if number of marks are odd

'''
from math import sqrt
from math import floor
import statistics

list = []
c = 0
while(int(c) >= 0):
    c = input("add marks : ")
    if (int(c) >= 0) :
        list.append(int(c))

def calculate_mean(list):
    return sum(list)/len(list)
    #return statistics.mean(list)

def calculate_variance(list):
    varience = 0
    mean = calculate_mean(list)
    for item in list:
        varience = varience + (item-mean)**2
    return varience/(len(list)-1)
    #return statistics.variance(list)
 
def calculate_standard_deviation(list):
    return sqrt(calculate_variance(list))
    #return statistics.stdev(list)

def calculate_sum(list):
    return sum(list)

def calculate_median(list):
    list.sort()
    mid = floor(len(list)/2)
    if len(list) % 2 == 0 :
        return (list[mid] + list[mid - 1]) / 2
    else:
        return list[mid]
    #return statistics.median(list)

print(calculate_mean(list))
print(calculate_variance(list))
print(calculate_standard_deviation(list))
print(calculate_sum(list))
print(calculate_median(list))