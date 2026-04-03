def main():
    with open("golf.txt", "w+") as file:
        name, score = get_user_info()

        write_info_to_file(file, name, score)

        file.seek(0)
        line = file.readline()

        while line != "":
            print(line)
            line = file.readline()


def get_user_info():
    name = input("Enter your name: ")
    score = input("Enter your score: ")

    return name,score


def write_info_to_file(file,name,score):
    file.write(name+"\n")
    file.write(score+"\n")


if __name__ == "__main__":
    main()