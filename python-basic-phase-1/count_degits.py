def countDigits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    print(count)

countDigits(233483)