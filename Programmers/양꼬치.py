def solution(n, k):
    b = 0
    if n >= 10:
        b = n // 10
        # (// : 몫, % : 나머지, / : 일반 나눗셈(소숫점))
        answer = (12000 * n) + 2000 * (k - b)
    else :
        answer = (12000 * n) + 2000 * k
    return answer
