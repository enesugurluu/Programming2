import random

file_random_size = int(input("how many random numbers the file will hold: "))

try:
    file = open("random.txt","w")
    for i in range(1,file_random_size+1):
        temp_random = random.randint(1,500)
        if i != file_random_size:
            file.write(str(temp_random)+ "\n")
        else:
            file.write(str(temp_random))

    file.close()

except FileNotFoundError:
    print("File not found.")