from more_itertools.more import rstrip


def main():
    file = open("file1.txt","w")
    number = int(input("Enter your number: "))
    #file.write(number) #Error: TypeError: write() argument must be str, not int
    file.write(str(number))
    file.close()

    file2 = open("file1.txt","r")
    file2_context = file2.read()

    print(file2_context)
    file2.close()

    file3 = open("file3.txt","r")
    file3_context = file3.read()


    for line in file3:
        print(line)

    file3.close()

    file4 = open("file3.txt","r")

    line = file4.readline()

    while line != "":
        print(line)
        line = file4.readline()



    """
    
    -readline() returns an iterator with each value being a string representing a single line.
    -readlines() returns a list of strings, with each string representing a single line of the file.
    -read() returns a string containing the entire content of the file.
    
    """


    file5 = open("file5.txt","r+")
    line = file5.readline()
    sum = 0
    while line != "":
        sum += int(line)
        line = file5.readline()

    print(f"Ortalama {sum/3}")

    print("Enes%%%".rstrip("%"))

    with open("file5.txt","r") as file:
        file5_context = file.read()
        print(file5_context)



    file6 = open("friends.txt","r+")
    line = file6.readline()
    while line != "":
        name, age,gpa = line.split(",")

        line = file6.readline()


if __name__ == "__main__":
    main()
