def solution(n, costs):
		# 비용을 기준으로 오름차순 정렬
    costs = sorted(costs, key=lambda x:x[2])
    node = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]

		# 크루스칼 알고리즘 (가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘)
		# 모든 정점을 잇는 네트워크 만들어질 때까지 
		# 비용이 적은 간선부터 하나씩 넣기
    while len(node) != n:
        for i in range(1, len(costs)):
						# 사이클이 발생하면 안되기 때문에, Union-Find 알고리즘 적용
            if costs[i][0] in node and costs[i][1] in node:
                continue
            if costs[i][0] in node or costs[i][1] in node:
                node.update([costs[i][0], costs[i][1]])
                answer += costs[i][2]
                break
    return answer
