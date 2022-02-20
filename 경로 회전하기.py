def solution(clothes):
    hash_dict={}
    for x, y in clothes:
        print(x,y)
        if(y in hash_dict.keys()):
            hash_dict[y]+=1
        else:
            hash_dict[y]=1
            
    tmp=1
    for x in hash_dict.values():
        # +1 을 해주는 이유는 해당 아이템을 착용하지 않는 경우 포함
        tmp*=(x+1)
    # 모든 종류를 안입는 경우는 없으므로 -1을 해주어야 한다.
    return tmp -1
