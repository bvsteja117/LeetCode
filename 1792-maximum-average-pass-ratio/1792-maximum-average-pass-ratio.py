from heapq import heappush, heappop
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def potential_improvement(pass_students, total_students):
        # Calculate how much the pass ratio will improve by adding one student
            return (pass_students + 1) / (total_students + 1) - pass_students / total_students
    
        # Convert to max heap by negating improvement
        heap = [(-potential_improvement(p, t), p, t) for p, t in classes]
        __import__('heapq').heapify(heap)
        
        # Distribute extra students to classes with most potential improvement
        for _ in range(extraStudents):
            _, p, t = __import__('heapq').heappop(heap)
            __import__('heapq').heappush(heap, (-potential_improvement(p + 1, t + 1), p + 1, t + 1))
        
        # Calculate final average pass ratio
        return sum(p / t for _, p, t in heap) / len(classes)