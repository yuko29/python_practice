s = input("")

normal = ""
reverse = ""

for i in s:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        normal += i.lower()



for i in s[::-1]:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        reverse += i.lower()

if normal == reverse:
    print("True")
else:
    print("False")
