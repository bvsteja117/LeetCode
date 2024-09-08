# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        current = head
        while current:
            n += 1
            current = current.next
        
        # get batch length
        batch_len = n // k
        extra_nodes = n % k

        # generate k batches
        arr = []
        current = head
        for _ in range(k):
            batch = current  # define head of current batch

            extra_one = 1 if extra_nodes > 0 else 0
            for i in range(batch_len + extra_one -1):
                if current:
                    current = current.next
            
            if current:  # switch, cut current batch, get head of next batch
                next_batch = current.next
                current.next = None  # cut current batch from next
                current = next_batch
            
            arr.append(batch)
            extra_nodes -= 1

        return arr