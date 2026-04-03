#While Loop
from sympy.codegen.ast import none

# x = 10
# while x > 5:
#     print(x)
#     x = x - 1
#
#
# y = 0
# while y < 10:
#     print(y)
#     y = y + 1
#
# n = 0
# while n < 10: n += 1;

#For Loop

for num in {1,2,3,4,5}:
    print(num)


for num in range(5): # O dan --> 4 e kadar 0,1,2,3,4
    print(num)

for num in range(1,6): # 1 den --> 5e kadar 1,2,3,4,5
    print(num)

# range(start, stop) Stop index won't be written

for num in range(1,10,2): print(num) # 1,3,5,7,9

# range(start, stop, step)

for num in range(5,0,-1): print(f"range : {num}") # 5, 4 ,3 ,2 ,1

# total = 0
# choosed = input("Would you like to continue? (Y/N): ")
# while choosed == "Y":
#     score = int(input("Enter your score: "))
#     total = total + score
#     print(f"Your total score is: {total}")
#     choose = input("Would you like to continue? (Y/N): ")

x = 10
x **= 2 #Shorthand operation

print(x) # Output: 100

# Nested Loop

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(f"{hours}:{minutes}:{seconds}")

# row = int(input("Enter a row number: "))
# column = int(input("Enter a column number: "))
#
# for r in range(row):
#     for c in range(column):
#         print("*",end="")
#
#     print()

n = 100

while n >= 25:
    print(n)
    n -= 1
else:
    print("Goodbye")

