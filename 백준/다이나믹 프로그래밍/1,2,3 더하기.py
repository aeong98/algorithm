# d[n]= n 을 1,2,3 의 조합으로 나타내는 방법
# d[n]=d[n-1]+d[n-2]+d[n-3]

t=int(input())

for _ in range(t):
    n=int(input())
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    dp[3]=4

    for i in range(4, n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    
    print(dp[n])
    
# Bottom-UP   
import sys
read = sys.stdin.readline

cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 11):
    cache[i] = sum(cache[i-3:i])

T = int(read())
for _ in range(T):
    print(cache[int(read())])


# Top-down

import sys
read = sys.stdin.readline

def dfs(num):
    if arr[num] > 0:
        return arr[num]
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        arr[num] = dfs(num-1) + dfs(num-2) + dfs(num-3)
        return arr[num]
     
T = int(sys.stdin.readline())
for _ in range(T):
    l = int(read())
    arr = [0] * (l+1)
    print(dfs(l))