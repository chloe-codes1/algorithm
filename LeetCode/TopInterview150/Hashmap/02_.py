class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()
        
        for a, b in zip(s, t):
            if a not in mapping:
                if b in used:
                    return False
                mapping[a] = b
                used.add(b)
            elif mapping[a] != b:
                return False
        
        return True

