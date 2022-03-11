def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    
    for com in range(n):
        if visited[com]==False:
            DFS(n, computers, com, visited)
            # DFS 로 최대한 컴퓨터들을 많이 방문하고 빠져나오게 되면 그것이 하나의 네트워크
            answer+=1

    return answer

def DFS(n, computers, com, visited):
    visited[com]= True
    for connect in range(n):
        # 연결된 컴퓨터
        if connect != com and computers[com][connect]==1:
            if visited [connect]==False:
                DFS(n, computers, connect, visited)