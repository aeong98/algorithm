
n=int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 격자 위에 있는지 판단
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 한 칸 상하좌우의 1 개수 세기
def adj_cnt(x,y):
    cnt=0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx,ny) and (arr[nx][ny] == 1):
            cnt += 1
    return cnt 

ans= 0 

for i in range(n):
    for j in range(n):
        if(adj_cnt(i,j) >= 3):
            ans +=1
       

print(ans)
