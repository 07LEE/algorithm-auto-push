import heapq

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return answer
    else:
        max_heap = [-w for w in works]
        heapq.heapify(max_heap)
        for i in range(n):
            max_work = heapq.heappop(max_heap)
            if max_work == 0:
                break
            heapq.heappush(max_heap, max_work + 1)
        for work in max_heap:
            answer += work ** 2
        return answer
