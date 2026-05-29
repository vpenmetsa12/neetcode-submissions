import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_tuples = {}
        return_list = []
        for x in nums:
            heap_tuples[x] = heap_tuples.get(x, 0) - 1
        test = [(value,key) for key, value in list(heap_tuples.items())]
        heapq.heapify(test)
        print(test) 
        for x in range(0,k):
            retVal = heapq.heappop(test)[1]
            print(retVal)
            return_list.append(retVal)
        return return_list

        