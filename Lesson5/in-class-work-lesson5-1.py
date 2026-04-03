"""

1. File Display
Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk. Write a program that displays all the numbers in the file.

"""


def main():
    with open("numbers.txt","r+") as file:
        line = file.readline()
        while line != "":
            print(line)
            line = file.readline()

if __name__ == "__main__":
    main()
