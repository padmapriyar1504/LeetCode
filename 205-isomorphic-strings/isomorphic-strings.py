class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        HM={}
        new=[]
        lenn=len(s)
        for i in range(lenn):
            if s[i] not in HM.keys():
                HM[s[i]]=t[i]
            else:
                value=HM[s[i]]
                if value!=t[i]:
                    return False
            if len(set(HM.keys()))!=len(set(HM.values())):
                    return False        
        return True                
                  
        