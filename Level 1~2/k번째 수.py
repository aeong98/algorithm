def solution(array, commands):
    answer = []
    for start, end, index in commands:
        new_array=sorted(array[start-1:end])
        answer.append(new_array[index-1])
    return answer
