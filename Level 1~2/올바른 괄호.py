def solution(s):
    answer = True
    stack=[]
    
    for s_ in s:
        if (len(stack)==0):
            stack.append(s_)
        else:
            tmp=stack[-1]
            if(tmp =="(" and s_==")"):
                stack.pop()
            else:
                stack.append(s_)
        
    if(len(stack)>0):
        return False
    else:
        return True
