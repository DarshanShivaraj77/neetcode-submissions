class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch.isalnum():
                st.append(ch.lower())
        l,r=0,len(st)-1
        while(l<=r):
            if(st[l]==st[r]):
                l+=1
                r-=1
            else:
                return False
        return True