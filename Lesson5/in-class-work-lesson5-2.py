def main():
    with open("names.txt","r") as file:
        line = file.readline()
        lines = 0

        while line != "":
            lines += 1
            line = file.readline()

        print(f"{lines} lines")


if __name__ == "__main__":
    main()