i = input().split()
a = int(i[0])
b = int(i[1])
a = a/100
a = a*a

bmi = b // a
print(int(bmi))
if bmi >= 25:
    print("Obesity")
