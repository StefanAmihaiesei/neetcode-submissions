class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frec = {}  # Folosim un dicționar în loc de listă
        
        for num in nums:
            if num in frec:
                return True
            
            frec[num] = 1
            
        return False