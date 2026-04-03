for row in range(7,0,-1):
    print("*"* row,end="")
    print()


#With Nested Loops
for row in range(7):
    for col in range(7-row):
        print("*",end="")
    print()