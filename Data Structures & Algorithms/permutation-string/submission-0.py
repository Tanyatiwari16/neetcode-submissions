class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False  # If s1 is longer, s2 can't contain its permutation
        
        # Frequency maps for s1 and the first window of s2
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])

        # If the first window is already an anagram
        if s1_count == s2_count:
            return True

        # Sliding window: Check the remaining substrings
        for i in range(len(s1), len(s2)):
            # Include the new character in the window
            s2_count[s2[i]] += 1
            # Remove the leftmost character from the window
            s2_count[s2[i - len(s1)]] -= 1

            # Clean up zero-count keys for direct comparison
            if s2_count[s2[i - len(s1)]] == 0:
                del s2_count[s2[i - len(s1)]]

            # Check if updated window matches s1_count
            if s1_count == s2_count:
                return True

        return False
