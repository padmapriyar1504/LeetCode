class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        HM={}
        new=[]
        lenn=len(pattern)
        s=s.split()
        if len(pattern)!=len(s):
            return False
        for i in range(lenn):
            if pattern[i] not in HM.keys():
                HM[pattern[i]]=s[i]
            else:
                value=HM[pattern[i]]
                if value!=s[i]:
                    return False    
            if len(set(HM.keys()))!=len(set(HM.values())):
                    return False            
        return True        