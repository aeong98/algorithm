# 동적 프로그래밍 기법과 유사
# 어떠한 칸에서 가장 큰 정사각형의 한변의 길이는 위, 왼쪽, 대각선 칸의 최소값에 1을 더한 것과 같다. (하나라도 0이 있으면 1로 기록됨)
def solution(board):
    answer = 0
    w= len(board[0])
    h=len(board)
    max_=0
    
    # 모든 요소가 0 일때, 0 반환
    zero=0
    for b in board:
        zero += b.count(0)
    if zero == w*h:
        return 0
    
    # 1개라도 1이 존재할때, 
    for i in range(1, h):
        for j in range(1, w):
            if board[i][j]==0:
                continue
            else:
                min_point = min(board[i-1][j-1], board[i][j-1], board[i-1][j])
                board[i][j]= min_point +1
                
                max_=max(max_, board[i][j])
    
    # (0,0), (1,0), (0,1) 중에 하나가 1일 경우
    if max_==0:
        return 1
    # 1보다 큰 가장 큰 정사각형이 존재하는 경우
    return max_**2
