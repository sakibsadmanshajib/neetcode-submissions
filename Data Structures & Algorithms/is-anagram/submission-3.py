class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        found = list(s)
        for _ in t:
            if _ in found:
                found.remove(_)
            else:
                return False
        return True