/**
1) n에 대해서 n-2 까지의 dp 값에 가로길이 2 짜리 타일로 만들수 있는 3가지 경우를 곱한 경우

-> dp[n-2] * 3
 

2) n에 대해서 0 ~ n-4 까지의 타일 뒤에 자신을 붙혀서 만들 수 있는 2가지 경우를 곱한 경우

-> ( dp[0] + dp[2] + ... dp[n-4] ) * 2


3) n에 대해서 가로 길이 n짜리의 새로운 타일 덩어리를 만드는 2가지 경우

-> 2
**/


/** 소스코드 **/


n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4,n+1) :
    if i%2 == 0 :
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else :
        dp[i] = 0
print(dp[n])
