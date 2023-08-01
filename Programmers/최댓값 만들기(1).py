def solution(numbers):
    answer = 0
    nlist = []
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if numbers[i] > numbers[j]:
                nlist = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = nlist
            
    return numbers[0] * numbers[1]
                
