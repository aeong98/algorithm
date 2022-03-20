
import sys
from collections import deque

def dfs(x):
    checked[x]=1
    print(x, end=" ")
    for i in graph[x]:
        if (checked[i]==0):
            dfs(i)

def bfs(x):
    queue=deque()
    checked[x]=1
    queue.append(x)
    
    while queue:
        y=queue.popleft()
        print(y, end=" ")
        for i in graph[y]:
            if(checked[i]==0):
                checked[i]=1
                queue.append(i)


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
checked = [0] * (n + 1)

# 인접 리스트 만들기
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
# 체크 배열 초기화
checked = [0] * (n + 1)
print()
bfs(v)