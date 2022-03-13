# d[n]= n개 팔아서 얻을 수 있는 수익 최대 수익
# d[n]= max( d[n-1]+ costs[0], d[n-2] +costs[1], d[n-3]+costs[2] ..) 
# 일반화
# d[n]=max( d[n-i]+p[i] (i: 1~n) )

import sys

n=int(input())
costs=sys.stdin.readline().rstrip()
d=[0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        d[i]=max(d[i], d[i-j]+costs[j-1])

print(d[n])