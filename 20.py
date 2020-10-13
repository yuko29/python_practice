ss = input()

s, n = ss.split(', ')

n = int(n)



for i in range(n):
    a = s[:-1]
    b = s[-1]
    s = b + a

print(s)
