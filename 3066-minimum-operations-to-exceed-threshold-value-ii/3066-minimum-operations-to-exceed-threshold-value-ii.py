class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Use heapq to efficiently maintain and access the smallest elements
        import heapq
        
        # Create a min heap from the input array
        heap = nums.copy()
        heapq.heapify(heap)
        
        operations = 0
        
        # Continue while we have at least 2 elements and the smallest is less than k
        while len(heap) >= 2 and heap[0] < k:
            # Get the two smallest elements
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            # Calculate new value according to the given formula
            new_value = min(x, y) * 2 + max(x, y)
            
            # Add the new value back to the heap
            heapq.heappush(heap, new_value)
            
            operations += 1
        
        # If we still have elements less than k, it's impossible
        if heap and heap[0] < k:
            return -1
            
        return operations