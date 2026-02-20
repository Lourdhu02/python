def sumOfFirstNnumbers(n : int):
    if n < 0 :
        print("Enter Valid Number")
    else:
        total = 0
        for i in range(1,n+1):
            total += i
        return total

print(sumOfFirstNnumbers(5))
