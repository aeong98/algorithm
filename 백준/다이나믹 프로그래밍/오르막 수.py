# d[n][l] : n자리 오르막 수, 마지막 수 l
# d[n][l] : sum(d[n-1][k]) (0<=k<=l)

n=int(input())
d=[[0 for _ in range(10)] for _ in range(n+1)]

for i in range(10):
    d[0][i]=1

for i in range(1,n+1):
    for j in range(10):
        for k in range(j+1):
            d[i][j]+=d[i-1][k]
 
print(d[n][9] % 10007)


