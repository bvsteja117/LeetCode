class Solution(object):
    def dividePlayers(self, skill):
        # Sort the skills to easily pair smallest with largest
        skill.sort()
        
        # The total skill of the first team (smallest + largest)
        total_skill = skill[0] + skill[-1]
        chemistry_sum = 0
        n = len(skill)
        
        # Loop to create pairs
        for i in range(n // 2):
            # Pair skill[i] with skill[n - 1 - i]
            if skill[i] + skill[n - 1 - i] != total_skill:
                return -1  # If total skill is not consistent, return -1
            chemistry_sum += skill[i] * skill[n - 1 - i]  # Add chemistry for valid pairs
        
        return chemistry_sum
