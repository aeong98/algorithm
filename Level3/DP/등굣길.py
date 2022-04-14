def solution(m, n, puddles):
    dp= [[0] * (n+1) for _ in range(m+1)]
    
    for pud in puddles:
        dp[pud[0]][pud[1]]=-1
        
    dp[1][0]=1
    
    for i in range(1,m+1):
        for j in range(1, n+1):
            # 물에 잠기면 갈 수 없음.
            if dp[i][j]==-1:
                dp[i][j]=0
            else:
                # 옆에서 오거나, 위에서 오거나
                dp[i][j]= (dp[i-1][j] + dp[i][j-1])% 1000000007
    
    return dp[m][n]
