def get_grades_and_calc_average():
    grades1 = int(input("Enter first grade: "))
    grades2 = int(input("Enter second grade: "))
    grades3 = int(input("Enter third grade: "))
    grades4 = int(input("Enter fourth grade: "))
    grades5 = int(input("Enter fifth grade: "))

    total_grades = grades1 + grades2 + grades3 + grades4 + grades5
    average = total_grades / 5

    return average

def calculateLetterGrade(*, average):
    if average >= 90:
        letterGrade = "A"
    elif average >= 80:
        letterGrade = "B"
    elif average >= 70:
        letterGrade = "C"
    elif average >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"
    return letterGrade



def main():
    average = get_grades_and_calc_average()

    letter_grade = calculateLetterGrade(average=average)
    print(f"5 Notun ortalaması : {letter_grade}")

main()


