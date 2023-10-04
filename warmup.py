name = "first letter"
print(name.capitalize())        #First letter
print(name.title())     #First Letter


name = input("pls enter the name")
if name == name[::-1]:   # reverses a string
    print("is palindrome")
else:
    print("is not palindrome")