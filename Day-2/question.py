'''
take input from user 16 digit credit card number
- card number must contain all digits
- it should not contain any upper case letter
- it should not contain any lower case letter
- it should not contain any space
- it should not contain any special char
- it should not have starting digit as 0
- last digit of card number should not be even
if all these checks pass, then card number is valid
user should get max 3 chance to enter right card number.
Use exception handling to solve this problem
'''
from sys import exc_info

count = 0
while(count <3):
    card = input("enter card no. \n")
    try : 
        if(len(card) != 16):
            raise print("Card digits must be 16")
        for c in card:
            if c.isupper():
                raise print("it should not contain any upper case letter")
            if c.islower():
                raise print("it should not contain any lower case letter")
            if c.isspace():
                raise print("it should not contain any space")
            if not c.isalnum():
                raise print("it should not contain any special char")
        if card[0] == '0':
            raise print("it should not have starting digit as 0")
        if int(card[15]) % 2 == 0:
            raise print("last digit of card number should not be even")
    except :
        count+=1
        if(count >=3):
            print("3 retries exhausted")
    else:
        print('OK')
        count = 3

count = 0
while(count <3):
    card = input("enter card no. \n")
    try : 
        assert len(card) == 16, "Card digits must be 16"
        for c in card:
            assert c.isupper(), "it should not contain any upper case letter"
            assert c.islower(), "it should not contain any lower case letter"
            assert c.isspace(), "it should not contain any space"
            assert not c.isalnum(), "it should not contain any special char"
        assert card[0] == '0', "it should not have starting digit as 0"
        assert int(card[-1]) % 2 == 0, "last digit of card number should not be even"
    except AssertionError:
        print(exc_info()[1])
        count+=1
        if(count >=3):
            print("3 retries exhausted")
    else:
        print('OK')
        count = 3