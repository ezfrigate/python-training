from sys import exc_info
input = input("enter time")
list = input.split(" ")
dict = {}
if len[list] == 6:
    dict[list[1]] = list[0]
print(list)
allowedHourSymbols = ["HRS", "HR", "HOURS", "HOUR"]
allowedMinuteSymbols = ["MINS", "MIN", "MINUTES", "MINUTE"]
allowedSecondSymbols = ["SECS", "SEC", "SECONDS", "SECOND"]
count = 0
# try :
#     assert int(list[0]), "Start has to be a number"
#     if list[1].upper() in  allowedHourSymbols:
#         count = count + 3600* int(list[0])
#         assert int(list[2]), "3rd part of input has to be a number"
#         if list[3].upper() in allowedMinuteSymbols:
#             count = count + 60* int(list[2])
#             assert int(list[4]), "5th part of input has to be a number"
#             if list[5].upper() in allowedSecondSymbols:
#                 count = count + int(list[4])
#             else:
#                 raise "format exception"
#         elif list[3].upper() in allowedSecondSymbols:
#             count = count + int(list[2])
#         else:
#             raise "format exception"
#     elif list[1].upper() in allowedMinuteSymbols:
#         count = count + 60* int(list[0])
#     elif list[1].upper() in allowedSecondSymbols:
#         count = count + int(list[0])
        
#     else:
#         raise "format exception"
# except :
#     print(exc_info()[0])
#     print(exc_info()[1])
try:
    if len(list) == 6 and list[1] in allowedHourSymbols and list[3] in allowedMinuteSymbols and list[5] in allowedSecondSymbols:
        print((int(list[0])*3600 + int(list[1])*60 + int(list[4]))*0.01)
    elif len(list) == 4 and list[1] in allowedMinuteSymbols and list[3] in allowedSecondSymbols:
        print((int(list[0])*60 + int(list[1]))*0.01)
    elif len(list) == 2 and list[1] in allowedSecondSymbols:
        print(int(list[4])*0.01)
    else:
        raise ("ex")
except:
    print("ex")
