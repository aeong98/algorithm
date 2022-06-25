N= int(input())
top_list = list(map(int, input().split()))
stack= [] 
answer = []


for i in range(N):
    while(stack):
        top =stack[-1]
        if(top[1] > top_list[i]):
            stack.append([i, top_list[i]])
            answer.append(top[0]+1)
            break
        else:
            stack.pop()
    
    if(len(stack)==0):
        stack.append([i, top_list[i]])
        answer.append(0)


print(" ".join(map(str, answer)))




