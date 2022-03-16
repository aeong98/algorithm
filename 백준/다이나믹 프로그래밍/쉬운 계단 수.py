# d[n][l] : n자리 계단 수, 마지막 수는 l
# d[n][l] : d[n-1][l-1]+d[n-1][l+1] (1<= l <= 8)
# 에외처리 필요
# d[n][0] : d[n-1][1]
# d[n][9] : d[n-1][8]

n=int(input())
d=[[0 for _ in range(10)] for _ in range(n+1)]
# 초기화
for i in range(1,10):
    d[1][i]=1

for i in range(2, n+1):
    for j in range(10):
        if(j>=1 and j<=8):
            d[i][j]=d[i-1][j-1]+ d[i-1][j+1]
        elif(j==0):
            d[i][j]=d[i-1][1]
        elif(j==9):
            d[i][j]=d[i-1][8]


print(sum(d[n])%1000000000)