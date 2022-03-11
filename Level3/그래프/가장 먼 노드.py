from collections import deque

def solution(n, edge):
    answer = 0
    # 노드 1부터 각 노드까지의 거리
    distance=[0]*(n+1)
    # 그래프 정보
    graph=[[] for _ in range(n+1)]
    # 방문 탐색할 queue
    queue=deque()
    
    for a,b in edge:
        # 양방향 그래프
        graph[a].append(b)
        graph[b].append(a)
    
    queue.append(1)
    distance[1]=1
    
    while queue:
        now=queue.popleft()
        for g in graph[now]:
            if distance[g]==0:
                queue.append(g)
                distance[g]=distance[now]+1
    
    # 가장 멀리떨어진 노드 거리
    max_edge=max(distance)
    # 개수
    for d in distance:
        if d==max_edge:
            answer+=1
        
    return answer