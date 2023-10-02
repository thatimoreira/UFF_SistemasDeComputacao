'''
Beecrowd: 1074
'''

n = int(input())

for i in range(n):
    num = int(input())
    
    if num == 0:
        print("NULL")
    else:
        if num > 0:
            posNeg = "POSITIVE"
        elif num < 0:
            num *= -1
            posNeg = "NEGATIVE"
        
        if num % 2 == 0:
            parImpar = "EVEN"
        else:
            parImpar = "ODD"
        
        print(parImpar, posNeg, end="\n")