def solution(skill, skill_trees):
    answer=0 
    
    for sk in skill_trees:
        # skill 을 list 로 반환
        skill_stack=list(skill)
        
        # skills 의 요소를 하나씩 불러들이며 반복
        for s in sk:
            # s가 skill 안에 있을 경우
            if s in skill:
                # 만약 가장 처음에 나타나는 문자가 아닐 경우
                if s!=skill_stack.pop(0):
                    break
        else:
            answer+=1
                    
                
        
    return answer
