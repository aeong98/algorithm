def dfs(x,a,board):
    global answer
    global visited 
    
    now=a[x]
    visited[x]=1
    
    # dfs 계속 진행함.가중치 더해줌.
    for i in board[x]:
        if visited[i]==0:
            now += dfs(i, a, board)
    
    # dfs가 끝나면, 가중치 answer에 더해줌.
    answer+=abs(now)
    
    return now

def solution(a, edges):
    global answer
    global visited 
    
    answer = 0
    length = len(a)
    visited = [0]*length
    board =[[] for _ in range(length)]
    
    if(sum(a)!=0):
        return -1
    
    for x, y in edges:
        board[x].append(y)
        board[y].append(x)
    
    dfs(0, a, board)

    return answer
