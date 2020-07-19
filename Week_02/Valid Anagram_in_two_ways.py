class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution1:
        # if len(s)!=len(t):
        #     return False
        # A  = [0 for i in range(256)]
        # for i in range(len(s)):
        #     tmp = ord(s[i])
        #     A[tmp] += 1
        # for i in range(len(t)):
        #     tmp = ord(t[i])
        #     A[tmp] -= 1
        # for i in range(256):
        #     if A[i] != 0:
        #         return False
        # return True

        #solution2:
        if len(s) != len(t):
            return False
        
        if set(s) != set(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False
            
        return True