def solution(numbers):
    answer = 0;
    checkList=[0,1,2,3,4,5,6,7,8,9];
    for num in checkList:
        if num not in numbers:
            answer+=num
    return answer
