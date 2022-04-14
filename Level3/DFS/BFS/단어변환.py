def bfs(begin, target, words, visited):
    stack = [(begin, 0)]
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            return depth
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            # 한글자로만 바꿀 수 있는지 확인
            for a,b in zip(cur, words[i]):
                if a!=b:
                    cnt += 1
            # 만약에 바꿀 수 있다면, bfs 진행
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth+1))
                
    return 0
                

def solution(begin, target, words):
    visited = [[False] for _ in range(len(words)+1)]
    
    result= bfs(begin, target, words, visited)
    return result
