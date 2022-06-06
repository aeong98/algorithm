# 16639. 괄호 추가하기
## DP : bottom-up
## 리스트에 최대값, 최소값을 모두 계산, 저장해야함(음수일때, 최소 * 최소 가 최대가 될 수 있기 때문에)

import sys
input = sys.stdin.readline

N = int(input())

n = N // 2

formula=input()

number, operator = [], []

for i, item in enumerate(formula):
    if i % 2 ==0:
        number.append(int(item))
    else:
        operator.append(item)

# bottop-up DP 로 풀기위한 리스트
# dp[i][j][0] = i ~j 까지의 최대값, dp[i][j][1] = i ~j 까지의 최소값,
dp = [[[0,0] for _ in range(n+1)] for _ in range(n+1)]

for scope in range(n+1):
    for i in range(0, n-scope+1):
        j = i+scope
        if i == j:
            dp[i][j][0]=number[i]
            dp[i][j][1]=number[i]
        else:
            tmp=[]
            for mid in range(i,j):
                if operator[mid] == "+":
                    tmp.append(dp[i][mid][0] + dp[mid+1][j][0])
                    tmp.append(dp[i][mid][0] + dp[mid+1][j][1])
                    tmp.append(dp[i][mid][1] + dp[mid+1][j][0])
                    tmp.append(dp[i][mid][1] + dp[mid+1][j][1])
                elif operator[mid] == "-":
                    tmp.append(dp[i][mid][0] - dp[mid+1][j][1])
                    tmp.append(dp[i][mid][0] - dp[mid+1][j][0])
                    tmp.append(dp[i][mid][1] - dp[mid+1][j][0])
                    tmp.append(dp[i][mid][1] - dp[mid+1][j][1])
                else:
                    tmp.append(dp[i][mid][0] * dp[mid+1][j][1])
                    tmp.append(dp[i][mid][0] * dp[mid+1][j][0])
                    tmp.append(dp[i][mid][1] * dp[mid+1][j][0])
                    tmp.append(dp[i][mid][1] * dp[mid+1][j][1])
            maxV, minV = max(tmp), min(tmp)
            dp[i][j][0]=maxV
            dp[i][j][1]=minV

print(max(dp[0][n]))
