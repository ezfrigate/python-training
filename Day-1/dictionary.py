# tuples are immutable lists and 10x faster access to items
tup =()

tup = (1,2,3)
print(type(tup))
print(1 in tup)

d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(d.keys())
print(d.values())
print(d.items())
d[4] = 4

print(d)




'''
1. take input from user key as roll number and name as value and store it in dictionary
do this infinitely till user enters 0 or negative roll number

2. once dictionary is created ask user roll number, if roll number is found print name of student
user should get max 3 chance to enter right roll number

3. take input name of student and create a list of all roll numbers having that name. search of
name should be case insensitive. if name not found, print "there is no student with this name"

'''

#PART 1
d = {}
roll = 1
while (int(roll) > 0):
    roll = input("Enter rollnumber \n")
    if int(roll) > 0:
        name = input("Enter student name \n")
        d[roll] = name

#PART 2
count = 0
found = 0
while count<3 and found==0:
    rollNToBeChecked = input("Enter rollnumber to find the student \n")
    count+=1
    if rollNToBeChecked in d.keys():
        print(d[rollNToBeChecked])
        found=1
if(found == 0):
    print("retries exhausted")

#PART 3
studentName = input("Find roll numbers with this Student name \n")
rollNListWithStudentName=[k for k, v in d.items() if v == studentName]
print("Roll numbers " + rollNListWithStudentName + " has name " + studentName)