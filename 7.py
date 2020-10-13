m = int(input("m: "))
n = int(input("n: "))

a = 1
b = 1
while True:
    c = a + b
    a = b
    b = c
    if c > n:
        break
    if c > m:
        print(c, end=' ')

#print('\n')
