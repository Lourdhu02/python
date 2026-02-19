def triangleType(a, b, c):
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

triangleType(3, 4, 3)
