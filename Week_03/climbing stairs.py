class Solution:
    def climbStairs(self, n: int) -> int:
        # sulution1:
        # array = []
        # array.append(1)
        # array.append(2)
        # if n == 1:
        #     return array[0]
        # if n == 2:
        #     return array[1]
        # if n>=3:
        #     for i in range(2,n):
        #         array.append(array[i-2]+array[i-1])
        #     return array[n-1]

        #solution2:
        if n==1:
            return 1
        if n==2:
            return 2
        if n>=3:
            var1 = 1
            var2 = 2
            for i in range(2,n):
                var1,var2 = var2,var1+var2
            return var2
