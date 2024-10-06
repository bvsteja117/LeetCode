
class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        # Split sentences into words
        s1 = sentence1.split()
        s2 = sentence2.split()
        
        # Ensure s1 is the longer sentence
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        # Check common prefix and suffix
        i = 0
        while i < len(s2) and s1[i] == s2[i]:
            i += 1
        
        j = 0
        while j < len(s2) - i and s1[len(s1) - 1 - j] == s2[len(s2) - 1 - j]:
            j += 1

        # If all of the words in the shorter sentence are either in the prefix or suffix of the longer one
        return i + j == len(s2)

        