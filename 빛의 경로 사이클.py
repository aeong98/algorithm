def solution(grid):
    global visited, n, m
    # 열의 길이
    n=len(grid)
    # 행의 길이
    m=len(grid[0])
    # 정답 리스트
    answer = []
    # 방문여부 체크 리스트 초기화
    visited= [[[False]*4 for _ in range(m)]for _ in range(n)]
    for x in range(n):
        for y in range(m):
            for d in range(4):
                # 방문한적이 없는 좌표, 방향이라면
                if not visited[x][y][d]:
                    result=simul(x,y,d,grid)
                    if(result != 0):
                        answer.append(result)
    answer.sort()
    return answer
    
    
def simul(x,y,d,grid):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]

    # global visited 배열을 사용하겠다.
    global visited
    # 사이클 경로 길이 저장 cnt
    cnt=0
    # 해당 경로 방문 체크
    visited[x][y][d]= True
    # 시작지점 저장
    x_,y_,d_=x,y,d
    # 반복문 시작
    while (1):
        # 모듈러 방식을 통해 순환 되는 경우도 체크
        x=(x+dx[d]) % n
        y=(y+dy[d]) % m
        # 경로 +1
        cnt +=1 
        
        # R 이면 우회전
        if (grid[x][y]=='R'):
            d=(d+1)%4
        # L 이면 좌회전
        elif (grid[x][y]=='L'):
            d=(d-1)%4
        # 방문한적이 있는 곳이고
        if (visited[x][y][d]):
            # 시작지점으로 돌아왔다면 경로 반환
            if (x,y,d)==(x_,y_,d_):
                return cnt
            # 시작지점이 아니면 0 반환
            else:
                return 0
        # 방문 체크
        visited[x][y][d]=True
            
    return answer
