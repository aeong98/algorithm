def calculate(parents, money, number, answer):
    # 종료조건 : 민호일때(center0) 또는 더이상 줄 돈이 없을 때,
    if parents[number]==number or money // 10 ==0:
        answer[number]+=money
        return
    # 부모노드에 보낼 돈
    send=money//10
    # 내가 가질 돈
    get=money-send
    answer[number]+=get
    calculate(parents, send, parents[number], answer)

def solution(enroll, referral, seller, amount):
    n=len(enroll)
    answer =[0] *(n+1)
    # 이름-번호 저장
    number={}
    # 자신의 부모를 나타내는 리스트
    parents = [i for i in range(n+1)]
    
    # 이름 -번호 초기화
    for i in range(n):
        number[enroll[i]]=i+1
    
    #추천인 저장
    for i in range(n):
        if(referral[i]!="-"):
            parents[i+1] = number[referral[i]]
        else:
            parents[i+1] = 0
            
    for i in range(len(seller)):
        calculate(parents, amount[i]*100, number[seller[i]], answer)
    return answer[1:]