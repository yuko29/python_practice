Input = input("file: ")

split = 0
index = [i for i in range(0, len(Input))]
index.reverse()
backslash = "\\"
for i in index:
    if Input[i] == '\\':
        split = i
        break

path = Input[0:i]
file = Input[i+1:]

print(path)
print(file)
