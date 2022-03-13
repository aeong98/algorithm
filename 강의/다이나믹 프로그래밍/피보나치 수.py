# 1. Top-Down

memo = [0] * (100)

def fibonacci (n):
    if (n<=1):
        return n
    else:
        if (memo[n] >0): #메모이제이션
            return memo[n]; 
        
        memo[n]= fibonacci(n-1) + fibonacci(n-2)
        return memo[n]


# 2. Bottom-Up

d = [0] * (100)

def fibonacci_(n):
    d[0]=0
    d[1]=1
    for i in range(2, n+1):
        d[i]= d[i-1]+d[i-2]

    return d[n]
