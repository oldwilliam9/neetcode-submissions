class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = []
        tList = []
        if len(s) != len(t):
            return False
            
        for n,i in enumerate(s):
            sList.append(s[n])
            tList.append(t[n])

        sList.sort()
        tList.sort()       
        if sList == tList:
            return True
        else:
            return False
        