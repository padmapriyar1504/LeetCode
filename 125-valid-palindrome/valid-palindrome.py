class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        arr=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                arr.append(i)
        arr=''.join(arr)        
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i]!=arr[j]:
                return False
                break
            else:
                i=i+1
                j=j-1
        return True            

        