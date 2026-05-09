class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for a in strs:
            sign = ''.join(sorted(a.lower()))
            if sign in group:
                group[sign].append(a)
            else:
                group[sign] = [a]

        return list(group.values())