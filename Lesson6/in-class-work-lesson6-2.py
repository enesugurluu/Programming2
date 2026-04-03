
try:
    file = open("random.txt","r")

    line = file.readline()
    counter = 0
    while line != "":
        print(line)
        line = file.readline()
        counter += 1

    file.close()

except FileNotFoundError:
    print("File not found.")