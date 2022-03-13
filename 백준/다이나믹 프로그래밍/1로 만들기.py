# Top-Down 으로 풀면 메모리 제한 때문에 런타임 에러 난다.

def go(n,d):
    # 전역 변수
    # n이 1일 때 초기화 
    if (n==1) :return 0
    # 메모이션되어 있을 때 값 바로 return
    if (d[n]>0): return d[n]
    # d[n]= d[n-1]+1
    d[n]=go(n-1)+1

    # d[n]= d[n/2]+1
    if(n%2 ==0):
        d[n]=min(d[n], go(n/2)+1)

    #d[n]= d[n/3]+1
    if(n%3==0):
        d[n]=min(d[n], go(n/3)+1)

    return d[n]

n=int(input())
d=[0]*(n+1)
print(go(n,d))     


# Bottom -up 으로 푸는것이 좋음
n=int(input())
d=[0]*(n+1)
d[1]=0

for i in range(2, n+1):
    d[i]=d[i-1]+1
    if i%2==0:
        d[i]=min(d[i], d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i], d[i//3]+1)

print(d[n])