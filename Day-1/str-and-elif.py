f = input("first name \n")
l = input("last name \n")

#count the number of chars in full name inclusing space 
#count upper case letters in full name 
#count lower case letters in full name
#count digits if any in full name
#count special chars if any in full name
#count spaces in full name
#count number of vowels (in any case) in full name

fn = f + " " + l
upper, lower, space, special, digit, vowel = 0,0,0,0,0,0
for c in fn:
    if c.isupper():
        upper+=1
    elif c.islower():
        lower+=1
    elif c.isspace():
        space+=1    
    elif c.isdigit():
        digit+=1
    else:
        special+=1
for c in fn:
    if c.upper() in "AEIOU":
        vowel+=1
print(upper, lower, space, special, digit, vowel)
