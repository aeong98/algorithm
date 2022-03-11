from collections import deque 

# 입력값이 크지 않기 때문에 bfs + 완전탐색으로 풀어도 문제 없다.
# 모든 연결 간선을 짤라본다. (이때, 한쪽만 순회하고, 나머지 영역은 빼서 구한다.)

def solution(n, wires):
    answer = 100000
    # 0 번 부터 노드가 시작되는 것이 아니기 때문에 +1 추가해주기
    graph=[[] for _ in range(n+1)]
    
    for s, e in wires:
        # 양방향 그래프
        graph[s].append(e)
        graph[e].append(s)
    
    for v1, v2 in wires:
        # 모든 노드 순회할 것이기 때문에, 매 순회마다 방문 배열을 만들기
        visited = [False for _ in range(n+1)]
        q= deque()
        q.append(v1)
        cnt = 1
        visited[v1]=True # 여기서 시작하기 때문에
        visited[v2]=True # 한쪽만 돌것이기 때문에
        
        # 순회하면서, 한쪽 그래프 노드의 개수 구하기
        while q:
            node= q.popleft()
            for v in graph[node]:
                if not visited[v]:
                    cnt +=1
                    visited[v]=True
                    q.append(v)
                    
        # 최솟값과 최대값 구하고, answer 갱신
        min_value= min (cnt, n-cnt)
        max_value = n-min_value
        answer = min (answer, max_value-min_value)
        

    return answer
