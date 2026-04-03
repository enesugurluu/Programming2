condition = True
value1 = "Test1"
value2 = "Test2"

if condition == True:
    print(value1)
if condition == False:
    print(value2)


condition = value1 if condition==True else value2
print(condition)