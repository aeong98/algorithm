import heapq

def solution(operations):
    answer = []
    heap=[]
    
    for op in operations:
        x,y=op.split(" ")
        # 힙에 원소 추가
        if(x=="I"):
            heapq.heappush(heap, int(y))
        # 최대값 삭제
        elif(x=="D" and int(y)==1):
            max_heap=[]
            for item in heap:
                heapq.heappush(max_heap, (-item, item))
            if(len(max_heap)>0):
                heapq.heappop(max_heap)
                heap=[]
                for x,y in max_heap:
                    heapq.heappush(heap, y)
        # 최솟값 삭제
        else:
            if(len(heap)>0):
                heapq.heappop(heap)
            
    if(len(heap)==0):
        return [0,0]
    else:
        return [max(heap), min(heap)]
            