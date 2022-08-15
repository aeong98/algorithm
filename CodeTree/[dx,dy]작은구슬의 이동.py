n,t= map(int,input().split())
x,y,dir_c =input().split()
x,y=int(x)-1, int(y)-1

dir_name={
    "U":2,
    "D":1,
    "R":0,
    "L":3,
}

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


cnt=0
dir_num = dir_name[dir_c]

for _ in range(t):
    # 미리 보기
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    # 격자 위에?
    if not in_range(nx, ny):  # check whether position is out of grid
        dir_num = 3 - dir_num # change direction
    else :
        x,y= nx, ny


print(x+1, y+1)
