class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_binary = bin(start)[2:].zfill(max(len(bin(start)[2:]), len(bin(goal)[2:])))
        goal_binary = bin(goal)[2:].zfill(max(len(bin(start)[2:]), len(bin(goal)[2:])))

        bit_flips = 0
        for i in range(len(start_binary)):
            if start_binary[i] != goal_binary[i]:
                bit_flips += 1

        return bit_flips