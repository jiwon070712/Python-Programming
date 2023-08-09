a,b,c = 5,6,7

#a,b = b,a
#a,c = c,a

temp = a
a = b
b = temp

temp = a
a = c
c = temp

print(a)
print(b)
print(c)
