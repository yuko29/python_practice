import math

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


n = int(input("n: "))

for i in range(n):
    if isPrime(i):
        print(i)