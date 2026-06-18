class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        d = {")":"(","]":"[","}":"{"}
        for each in s:
            if each in ("(", "[","{"):
                stack.append(each)
            elif each in d:
                if not stack or stack.pop()!=d[each]:
                    return False
        return len(stack)==0
        