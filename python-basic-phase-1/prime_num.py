def primeNumber(n):
    if n == 0:
        print("not prime")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print("not prime")
                break
        else:
            print("prime")


primeNumber(11)
