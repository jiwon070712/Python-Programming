def solution(numbers):
    c = 0
    for i in numbers:
        c = c + i
    answer = c / len(numbers)
    return answer

# c++ : length(numbers) / sizeof(numbers[0])
#  8(길이) * 8(바이트) = 64 / 8(바이트)  => 8(길이)      
