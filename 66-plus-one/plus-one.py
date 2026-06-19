class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(map(str,digits))
        result = int(s)+1
        ans = list(map(int,str(result)))

        return ans
        