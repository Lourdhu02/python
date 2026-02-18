def leapYearCheck(year : int):
    status = year % 4
    if status == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
leapYearCheck(2024)