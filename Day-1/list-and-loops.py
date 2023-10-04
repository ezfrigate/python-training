'''
places = ['Delhi', 'Mumbai', 'CHENNAI', 'Jaipur']
attractions = ['Red Fort','Gateway of India', 'Marina Beach', 'Amer Fort']

ques 1:- print messages
Delhi has an attraction Red Fort
Mumbai has an attraction Gateway of India
..
...

ques 2:- take input from user any place and print its attraction
user should get max 3 chance to enter the right place. if all attempts fails print Failure
at any point user enters the right place, print its attraction and do not ask again
search of place should be case insensitive
'''

places = ['Delhi', 'Mumbai', 'CHENNAI', 'Jaipur']
attractions = ['Red Fort','Gateway of India', 'Marina Beach', 'Amer Fort']
#Q1
i = 0
while(i<4):
    print(places[i] + "has an attraction" + attractions[i])
    i+=1
#OR
for index in range(len(places)):
    print(places[index]+' has an attraction'+attractions[index])

#Q2
count = 0
found = 0
while count < 3 and found == 0:
    place = input("Enter a place \n")
    count+=1
    for item in places:
        if item.lower() == place.lower():
            print(attractions[places.index(item)])
            found = 1
if(found == 1):
    print("3 wrong inputs in a row")