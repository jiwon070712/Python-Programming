n = int(input())
if n%2 == 1 and n%3 == 0:
    answer = "true"
elif n%2 == 0 and n%5 == 0:
    answer = "true"
else :
    answer = "false"

print(answer)
