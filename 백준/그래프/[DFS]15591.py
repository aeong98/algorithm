import sys
from collections import deque
input = sys.stdin.readline

N, Q= map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]


def find_video(v, k, graph):
    visited = [False] * (N+ 1)
    visited[v] = True
    result = 0
    q = deque([(v, float('inf'))])

    while q:
        v, usado = q.pop()
        for next_v, next_usado in graph[v]:
            next_usado = min(usado, next_usado)
            if next_usado >= k and not visited[next_v]:
                result += 1
                q.append((next_v, next_usado))
                visited[next_v] = True
    return result

for _ in range(N-1):
    p,q,r=map(int, sys.stdin.readline().split())
    graph[p].append((q,r))
    graph[q].append((p,r))


for _ in range(Q):
    k, v=  map(int, sys.stdin.readline().split())
    print(find_video(v, k, graph))
