def solution(citations):
    citations.sort()
    print(citations)
    max_num=-1
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations)-i
    return 0
