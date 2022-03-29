def solution(n, results):
    # 진경우 -1, 이긴경우 1, 모르는 경우 0
    graph=[[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for a,b in results:        
        graph[a][b] = 1
        graph[b][a] =-1
         
    # 플로이드 와샬
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1,n+1):
                if graph[i][j] == 0:
                    continue
                
                # i와 j -> j와 k => i와 k의 순위를 알 수 있음.
                if graph[i][j]==graph[j][k]:
                    graph[i][k]=graph[i][j]
                    graph[k][i]=-graph[i][j]
                    
    answer= 0
    for i in range(1, n+1):
        # 정확히 순위를 모르는 경우가 단 한개라도 있으면
        if 0 in graph[i][1:i] + graph[i][i+1:]:
            continue
        # 모든 순위를 알고있으면 (즉, 0이 자기자신 말고 없는 경우)
        answer+=1
        
    return answer
