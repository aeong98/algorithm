# 17780 새로운게밍
## 구현, 시뮬레이션

import sys
input = sys.stdin.readline

dx= [0, 0, -1, 1]
dy= [1, -1, 0, 0]

N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

# 체스말 쌓인 순서대로 저장
chess_map = [[[] for _ in range(N)] for _ in range(N)]
# 체스 말의 좌표와 방향을 저장
chess = [0 for _ in range(K)]


for i in range(K):
    x, y, z = map(int ,input().split())
    chess_map[x-1][y-1].append(i)
    chess[i]= [x-1, y-1, z-1]

def move(chess_num):
    x, y ,z = chess[chess_num]

    # 입력받은 말의 번호와, 말이 있는 좌표 맨 밑에 있는 말의 번호가 다르면 return
    if chess_num != chess_map[x][y][0]: 
        return 0 
    
    nx=x+dx[z]
    ny=y+dy[z]

    if not 0<= nx < N or not 0<= ny < N or a[nx][ny] == 2:
        # 방향 반대로 바꾸기
        if 0 <= z <= 1:
            nz= (z+1)%2
        else:
            nz = (z-1)%2 +2
        chess[chess_num][2]=nz
        nx = x+ dx[nz]
        ny = y +dy[nz]
        if not 0 <=nx < N or not 0<=ny <N or a[nx][ny]==2:
            return 0

    # 이동할 체스 묶음 저장
    chess_set =[]
    chess_set.extend(chess_map[x][y])
    # 해당 좌표 초기화
    chess_map[x][y]=[]

    # 방향 바꿈 
    if a[nx][ny] == 1:
        chess_set = chess_set[-1::-1]

    # 체스 말들을 다음 칸으로 이동하고 말의 좌표를 갱신한다.
    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx, ny]

    # 쌓인 말의 개수가 4 이상이면 1을 리턴하고 cnt 를 출력한다. 
    if(len(chess_map[nx][ny]) >= 4):
        return 1
    
    return 0


cnt =1 
while cnt <= 1000:
    for i in range(K):
        flag=move(i)
        if flag :
            print(cnt)
            sys.exit()
    cnt +=1 

print(-1)


