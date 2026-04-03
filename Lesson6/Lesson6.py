#Lists

item1 = 2
item2 = 3
item3 = 4

list = [item1, item2, item3]

sum = 0
for item in list:

    sum += item

print(sum)

index = 0
sum2 = 0

try:
    entered = int(input(f"Enter an index number between 0 and {len(list)-1}: "))
    print(list[entered])

except IndexError:
    print("IndexError")
