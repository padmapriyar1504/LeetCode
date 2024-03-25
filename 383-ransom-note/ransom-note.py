class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        j=0
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                magazine = magazine.replace(i, "", 1)

                continue
            j+=1    
        return True            
        