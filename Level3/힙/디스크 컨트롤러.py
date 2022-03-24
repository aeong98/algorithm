import heapq

def solution(jobs):
    answer = 0
    # 현재 시점
    now=0
    # 시작시간
    start=-1
    heap=[]
    i=0
    
    while i < len(jobs):
        # 현재 시점에서 선택할 수 있는 job들 우선순위큐에 넣기
        for j in jobs:
            if start < j[0] <=now:
                # 소요시간 순으로 정렬해야되기 때문에 순서 바꿔줌.
                heapq.heappush(heap, [j[1], j[0]])
        # 현재 시점에서 선택할 수 있는 job 이 있다면
        if len(heap) >0:
            # 가장 빨리끝나는 job 선택 
            select = heapq.heappop(heap)
            # 시작시간을 현재시간으로 바꿔줌
            start =now 
            # 끝나는시점 구하기
            now +=select[0]
            # 끝난 시간에서 job 들어온 시간 빼주기
            answer += (now - select[1])
            i+=1
        # 현재 선택할 수 있는 시간이 없다면 시간 더해주기
        else:
            now +=1 
            
            
    return int(answer/len(jobs))