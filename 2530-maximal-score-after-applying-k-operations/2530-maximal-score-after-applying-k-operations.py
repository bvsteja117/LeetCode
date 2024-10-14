import heapq

class Solution(object):
    def maxKelements(self, nums, k):
        # Convert the list into a max heap by negating the elements
        nums = [-x for x in nums]
        heapq.heapify(nums)
        score = 0

        for i in range(k):
            # Pop the largest element from the heap (smallest negative number)
            x = -heapq.heappop(nums)
            score += x

            if x == 1:
                score += (k - 1 - i)
                break

            # Push the new element after applying (x + 2) // 3
            heapq.heappush(nums, -(x + 2) // 3)

        return score
