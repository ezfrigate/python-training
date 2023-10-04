from math import pi
#Return multiple values from a function in tuple

def fun(a,b):
    return a+b, a-b

ans = fun(4,3)
print(type(ans))
print(ans[0])
print(ans[1])


'''
1. take input radius in a function and return to main
in area function find area and return to main and print it
in perimeter function find perimeter and print its perimeter


2. take input name, age and gender in a function and return to main
in check_name :- count the number of vowels in name, irrespective of case
in check_age :- print adult if age>18 otherwise not adult
in check_gender :- print YES if gender is Male or M or MALE in any case
                   print NO if gender is female or Female or F in any case

'''
name = input("enter radius \n")
def area(rad):
    return pi* rad**2

def peri(rad):
    return 2* pi* rad

print("Area of the circle is " + str(area(3)))
print("Perimeter of the circle is " + str(peri(3)))

def take_inputs():
    name = input("enter name \n")
    age = input("enter age \n")
    gender = input("enter gender \n")
    return name, age, gender

def check_name(name):
    count = 0
    for c in name:
        if c.upper() in "AEIOU":
            count+=1
    return count

check_age = lambda age: "adult" if int(age) > 18 else "not adult"

def check_gender(gender):
    if gender.upper() == "M" or gender.upper() == "MALE":
        return "YES"
    if gender.upper() == "F" or gender.upper() == "FEMALE":
        return "NO"
    
tup = take_inputs()

print("There are " + str(check_name(tup[0])) + " vowels in your name.")
print(check_age(tup[1]))
print(check_gender(tup[2]))