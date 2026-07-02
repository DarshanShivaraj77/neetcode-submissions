class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for char in s:
            if char.isalnum():
                res.append(char.lower())

        for i in range(len(res)//2):
            if res[i]!=res[len(res)-i-1]:
                return False

        return True