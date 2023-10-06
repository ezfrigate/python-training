try:
    num1 = 10
    num2 = 0
    ans = num1/num2
except ZeroDivisionError:
    print("don't divide by zero")
except ValueError:
    print("cannot divide strings")
except: #defaulterror
    print("something went wrong")
else:
    print("ans is ", ans)
finally:
    print("bye")

'''
1. create a dictionary where key is emp id and value is name of employee.
keep on taking key value pairs till user enters 0 or -ve emp id

once dictionary is created ask user any emp id and print name of that employee
if emp id does not exist, trap an exception and print message emp not found

2. take input any string and try to replace all vowels with XX. if there is no vowel print
message no vowel is present. use exception handling if needed
'''

#PART 1
dict = {}
id = 0
try:
    while(int(id) >= 0):
        id = input("enter key : \n")
        if(int(id) >= 0):
            name = input("enter value : \n")
            dict[id] = name
except:
    print("Strings can not be set as keys")

print(dict)

input = input("Enter your employee ID : \n")
try : 
    print(dict[id])
except :
    print("no employee found with this id")

#PART 2
s = "jwebfiubrfibwlnlkwbhjv"
for c in "aeiouAEIOU":
    s = s.replace(c, "XX")
print(s)