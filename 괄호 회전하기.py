def solution(s):
    answer=0
    for i in range(len(s)):
        # 한칸씩 회전한 문자열 만들기 
        right = s[:i]
        left =s[i:]
        new =left+right
        stack=[new[0]]
        
        # 해당 문자가 괄호가 정상적인지 stack으로 확인
        for j in range(1,len(new)):
            # 스택에 원소가 있을 때,
            if(len(stack)>0):
                # 마지막 문자와 새로운 문자가 매칭된다면 pop
                if(stack[-1]=='[' and new[j]==']'):
                    stack.pop()
                elif (stack[-1]=='{' and new[j]=='}'):
                    stack.pop()
                elif(stack[-1]=='(' and new[j]==')'):
                    stack.pop()
                # 그렇지 않다면 push
                else:
                    stack.append(new[j])
            # 스택에 원소가 없다면 push
            else:
                stack.append(new[j])
                
         
         # 스택에 남아있는 원소가 없다면, 모든 원소가 매칭되어 pop 됐다는 소리이므로, 정답에 추가
        if(len(stack)==0):
            answer+=1;
            
     
    return answer
