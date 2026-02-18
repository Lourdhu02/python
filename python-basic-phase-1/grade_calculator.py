def gradeCalculator(g: int):
    if 90 <= g <= 100:
        print("A")
    elif 80 <= g < 90:
        print("B")
    elif 70 <= g < 80:
        print("C")
    elif 60 <= g < 70:
        print("D")
    elif 0 <= g < 60:
        print("F")
    else:
        print("Invalid Score")
gradeCalculator(54)
