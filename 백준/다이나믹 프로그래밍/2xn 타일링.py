# d[i] = 2*i 직사각형을 채우는 방법의 수
# dp[n]= dp[n-2]+2 + dp[n-1]+1

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3,1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)