class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        f = list(s)
        for _ in t:
            if _ not in f:
                return False
            else:
                f.remove(_)
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        for a in strs:
            found = False
            for item in group:
                if self.isAnagram(item[0], a):
                    item.append(a)
                    found = True
                    break
            if not found:
                group.append([a])

        return group