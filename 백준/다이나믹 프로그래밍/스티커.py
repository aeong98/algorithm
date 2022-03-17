# 0 XX
# 1 OX
# 2 XO
# d[n][s] = 2*n 스티커 n번열의 상태가 s라는 것의 점수
# a[i][j] = i행 j열의 스티거커 점수
# d[n][0] = max(d[n-1][0], d[n-1][1], d[n-1][2]) 
# d[n][1] = max(d[n-1][0], d[n-1][2]) + a[n][1]
# d[n][2] = max(d[n-1][0], d[n-1][1]) +a[n][2]
# 정답 = max(d[n][0], d[n][1], d[n][2])

import sys

T=int(input())

def solution(n):
    d=[[0 for _ in range(3)] for _ in range(n+1)]
    a=[list(map(int, sys.stdin.readline().split())) for _ in range(2)]


    d[1][1]=a[0][0]
    d[1][2]=a[1][0]

    for i in range(2,n+1):
        d[i][0]=max(d[i-1][0], d[i-1][1], d[i-1][2])
        d[i][1]=max(d[i-1][0], d[i-1][2]) + a[0][i-1]
        d[i][2]=max(d[i-1][0], d[i-1][1]) + a[1][i-1]
       
    print(max(d[n][0], d[n][1], d[n][2]))
    
for i in range(T):
    N=int(input())
    solution(N)

 