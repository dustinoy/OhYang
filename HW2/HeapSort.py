class Solution(object):
    def HS(self,nums):     
        n = len(nums)   
        start = n // 2 - 1
        for i in range(start, -1, -1):   
            self.heapify(n, i)   
        for i in range(n-1, 0, -1):   
            nums[i],nums[0]=nums[0],nums[i]   
            self.heapify(i, 0)
    def heapify(self,n,i):
        max=i
        l=2 * i + 1  
        r=2 * (i + 1)    
        if l < n and nums[i] < nums[l]:   
            max = l   
        if r < n and nums[max] < nums[r]:   
            max = r   
        if max != i:   
            nums[i],nums[max]=nums[max],nums[i]   
            self.heapify(n, max)   

Solution().HS(nums)
print(nums)
