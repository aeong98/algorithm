def solution(triangle):
    answer = 0
    dp=[]
    for i in range(len(triangle)):
        dp.append([0 for j in range(i+1)])
        
    dp[0][0]=triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 갈 수 있는 경우의 수
            tmp=triangle[i][j]
            if(j-1>=0):
                tmp = triangle[i][j] + triangle[i-1][j-1]
            if(j<len(triangle[i-1])):
                tmp = max(tmp, triangle[i-1][j]+triangle[i][j])
                
            triangle[i][j] =tmp

    return max(triangle[len(triangle)-1])
