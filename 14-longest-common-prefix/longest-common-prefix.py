class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = min(strs, key =len)
        result = ""
        for i in range(len(temp)):
            for each in strs:
                if temp[i]!=each[i]:
                    return result
            result +=temp[i]
        return result
        