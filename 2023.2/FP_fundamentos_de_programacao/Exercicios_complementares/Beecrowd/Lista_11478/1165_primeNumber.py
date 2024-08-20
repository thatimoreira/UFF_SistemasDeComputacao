testsNumber = int(input())

for k in range(testsNumber):
    n = int(input())

    if n == 0 or n == 1:
        print("%d nao eh primo" %n)
    else:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
        if prime == True:
            print("%d eh primo" %n)
        else:
            print("%d nao eh primo" %n)
