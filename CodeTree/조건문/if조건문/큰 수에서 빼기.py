i = input().split()
a = int(i[0])
b = int(i[1])
if a < b:
    m = a
    a = b
    b = m

print(a - b)
