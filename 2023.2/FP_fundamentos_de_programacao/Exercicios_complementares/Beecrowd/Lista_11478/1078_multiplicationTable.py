n = int(input())

if n >= 1 and n <= 1000:
    print("1 x %d = %d" %(n, n))
    for i in range(2, 11):
        mult = i * n
        print("%d x %d = %d" %(i, n, mult))
else:
    n = int(input())