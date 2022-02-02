from collections import deque
# BFS
# 모든 말단 노드를 탐색한 후 target 에 만족하는 값이 되는지를 검사한다.

def solution(numbers, target):
		# 정답
    answer = 0
    # BFS 탐색을 위한 queue 생성
    queue=deque()
    # queue 초기화 (첫번째 숫자 + - 한 경우)
    queue.append([-numbers[0],0])
    queue.append([+numbers[0],0])
    
    # 탐색시작
    while queue:
        num, i=queue.popleft()
        # 말단 노드이면 target 과 비교
        if i==len(numbers)-1:
            # target 과 같으면 answer 에 추가 
            if num == target:
                answer += 1
        # queue 에 가능한 경우의수 추가 (노드 추가)
        else:
            queue.append([num-numbers[i+1], i+1])
            queue.append([num+numbers[i+1], i+1])
            
    return answer
