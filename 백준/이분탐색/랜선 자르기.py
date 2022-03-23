# 랜선 K 개 
# 랜선을 같은 길이로 잘라서 N 개를 만들어야 한다.
# 예를들어, 랜선이 4개가 있고 11개 이상 만들어야하는 경우
# X 로 자르면, N 개 이상이 나옴 ? YES -> X 증가 / NO -> X 감소
# left =1, right = 가장 길이가 긴 랜선


# X 로 잘랐을 때, 원하는 숫자보다 큰지 
def check(x):
    global line
    global m
    cnt =0
    for i in range(n):
        cnt +=line[i]//x
    return cnt >=m

n,m=map(int, input().split(" "))
line=[]
max_=0
ans = 0

for i in range(n):
    tmp=int(input())
    line.append(tmp)
    max_ =max(max_,tmp)

l=1
r=max_

while(l<=r):
    mid=(l+r)//2
    if(check(mid)):    # YES -> X 증가 시킴
        if(ans < mid):
            ans=mid
        l=mid+1
    else:
        r=mid-1        #  NO -> X 감소 시팀

print(ans)

