# 1. Bottom-Up
# - 초기화
# - 점화식 : f(n) = f(n-2) + f(n-1)


n=int(input())
dp=[0]*(n+1)
dp[1]=1
dp[2]=2

for i in range(3, n+1):
    dp[i]=dp[i-2]+dp[n-1]

print(dp[n])


# 2. Top-Down
# - 재귀, 메모이제이션
if __name__=="__main__":
    n=int(input())
    dp=[0]*(n+1)
    print(dfs(n))

def dfs(len):
    # 메모이제이션 (이미 값이 있을 경우에는 return)
    if dp[len]>0:
        return dp[len]
    # 종료 시점 명시
    if(len ==1 or len==2):
        return len
    else:
        dp[len]=dfs(len-1)+ dfs(len-2)
        return dp[len]


