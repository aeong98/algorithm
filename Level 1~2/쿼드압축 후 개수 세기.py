def solution(arr):
    result =[0,0]
    L=len(arr)
    
    def divide(a,b,l):
        start =arr[a][b]
        # 정사각형 내 모든 원소가 똑같은지 확인
        for i in range(a, a+l):
            for j in range(b,b+l):
                # 하나라도 다르면 압축하지 못한다.
                if (arr[i][j]!=start):
                    # 4등분으로 쪼개줘야함. (재귀로 돌림)
                    ll=l//2
                    divide(a,b,ll)
                    divide(a,b+ll, ll)
                    divide(a+ll,b,ll)
                    divide(a+ll,b+ll,ll)
                    return
                
        # 모든 원소가 똑같으면 +1
        result[start]+=1

    divide(0,0,L)
    return result
