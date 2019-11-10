class Solution(object):
    def HS(self,nums):     
        n = len(nums)   
        start = n // 2 - 1
        for i in range(start, -1, -1):   
            self.heapify(nums,n, i)   
        for i in range(n-1, 0, -1):   
            nums[i],nums[0]=nums[0],nums[i]   
            self.heapify(nums,i, 0)
    def heapify(self,nums,n,i):
        max=i
        l=2 * i + 1  
        r=2 * (i + 1)    
        if l < n and nums[max] < nums[l]:   
            max = l   
        if r < n and nums[max] < nums[r]:   
            max = r   
        if max != i:   
            nums[i],nums[max]=nums[max],nums[i]   
            self.heapify(nums,n, max)   
a = [-2,-5,-98,-46,-3,-21,-69,-98,-54,-31]
Solution().HS(a)
print(a)
