from numpy.ma.extras import average


def main():
    with open("numbers.txt","r") as file:
        line = file.readline()

        total_sum = 0
        lines = 0

        while line != "":
            lines += 1
            total_sum += int(line)
            line = file.readline()

        print(f"Average is {total_sum/lines:.1f}, Sum is {total_sum}, and Total lines is {lines}")


if __name__ == "__main__":
    main()