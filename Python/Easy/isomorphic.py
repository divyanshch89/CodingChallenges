class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        transform_s = []
        transform_t = []
        d_s={}
        for i,c in enumerate(s):
            if c not in d_s:
                d_s[c]=i
                transform_s.append(i)
            else:
                transform_s.append(d_s[c])
        d_s = {}
        for i,c in enumerate(t):
            if c not in d_s:
                d_s[c]=i
                transform_t.append(i)
            else:
                transform_t.append(d_s[c])
        
        return transform_s==transform_t
        