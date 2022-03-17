# 포도주 시식 (커밋 테스트)
# d[i][j] : i번쨰 포도주가 j 번째 연속으로 먹은 경우 포도주의 양 (0<=j<=2)
# d[i][0] : max(d[i-1][0], d[i-1][1], d[i-1][2])
# d[i][1] : d[i-1][0] + a[i]
# d[i][2] : d[i-1][1] + a[i]
# 정답 max(d[n][0], d[n][1], d[n][2])


n=int(input())
d=[[ 0 for _ in range(3) ] for _ in range(n+1)]
a=[0]

for i in range(n):
    a.append(int(input()))

d[1][0]=0
d[1][1]=a[1]

for i in range(2,n+1):
    d[i][0]=max(d[i-1][0], d[i-1][1], d[i-1][2])
    d[i][1]=d[i-1][0]+a[i]
    d[i][2]=d[i-1][1]+a[i]


print(max(d[n][0], d[n][1], d[n][2]))
