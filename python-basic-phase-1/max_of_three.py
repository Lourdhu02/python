def maxOfThree(a,b,c):
    if a > b:
        max = a
        if a > c:
            max = a
        else:
            max = c
    else:
        max = b

    print(max)
maxOfThree(24,6,29)