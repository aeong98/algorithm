import heapq
INF=int(1e9) #무한을 의미하는 값으로 10억 설정

def solution(N, road, K):
    answer=0
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
    graph = [[] for _ in range(N+1)]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (N+1)
    
    # 간선 정보 입력받기
    for a,b,c in road: 
        # 양방향
        graph[a].append([b,c])
        graph[b].append([a,c])
    
    def dijkstra(start):
        q=[]
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
        heapq.heappush(q,(0,start))
        distance[start]=0
        # 큐가 비어있지 않으면
        while q :
            # 가장 최단 거리가 짧은 노드 정보 꺼내기
            dist, now=heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있다면
            if distance[now] <dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드라면 무시
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 cost 가 더 적다면 최단 거리 테이블 갱신
                if cost <distance[i[0]]:
                    distance[i[0]]=cost
                    heapq.heappush(q, (cost, i[0]))
                    
    # 다익스트라 알고리즘 수행
    dijkstra(1)
    
    # 모든 최단 거리중 K 이하인 원소의 개수 출력
    for i in range(1, N+1):
        if distance[i] <= K:
            answer+=1
    
    return answer
