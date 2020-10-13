h = int(input("Unput a number: "))
for i in range(1, h+1, 2):
    space = int((h-i)/2)
    s = ' ' * space
    p = "*" * i
    row = s+p+s
    print(row)