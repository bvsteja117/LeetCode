class Solution(object):
    def checkInclusion(self, s1, s2):
        from collections import Counter

        len_s1 = len(s1)
        len_s2 = len(s2)

        # Base case: if s1 is longer than s2, return false
        if len_s1 > len_s2:
            return False

        # Count the frequency of characters in s1
        s1_count = Counter(s1)
        # Count the frequency of characters in the first window of s2
        s2_count = Counter(s2[:len_s1])

        # Function to compare two counters
        def matches(counter1, counter2):
            return all(counter1[char] == counter2[char] for char in counter1)

        # Check the initial window
        if matches(s1_count, s2_count):
            return True

        # Slide the window over s2
        for i in range(len_s1, len_s2):
            # Add the new character to the current window
            s2_count[s2[i]] += 1
            # Remove the character that is sliding out of the window
            s2_count[s2[i - len_s1]] -= 1

            # Clean up the counter to avoid having zero counts
            if s2_count[s2[i - len_s1]] == 0:
                del s2_count[s2[i - len_s1]]

            # Check if the current window matches the frequency of s1
            if matches(s1_count, s2_count):
                return True

        return False
