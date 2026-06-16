class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        result = 0
        INT_MAX = 2**31-1
        while temp!=0:
            n= temp%10
            if result>(INT_MAX-n)//10:
                return 0
            result = result*10+n
            temp =temp//10
        return -(result) if x<0 else result
        