class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def rec(left, right, n , strs):
            if left==n and right == n:
                result.append(strs)
                return
            if left < n:
                rec(left +1,right,n,strs+"(")
            if right < left:
                rec(left,right+1,n,strs+")")

        rec(0,0,n,"")
        return result