a = 0
b = 0
i = int(input())



#for e in range (i-1):
#    print('')
#    for j in range(i-1-e):
#        print(" ",end = '')


print(end = '')
for e in range (i):
    for j in range(i - e - 1):
        print('-', end = '')
        
    for j in range(e+1):
        print('*', end = '')
    print('')
