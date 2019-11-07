class Solution(object):
    def MS(self, nums):
        if len(nums)<=1:
            return nums
        else:  
            new=[]
            n=len(nums)
            mid=int(n//2)
            l=Solution().MS(nums[:mid])
            r=Solution().MS(nums[mid:])
        l_index=0
        r_index=0    
        while (len(l)>l_index) and (len(r)>r_index):          
            if l[l_index]<r[r_index]:
                new.append(l[l_index])
                l_index+=1
            else:
                new.append(r[r_index])
                r_index+=1
        new.extend(l[l_index:])
        new.extend(r[r_index:])
        return new
            
a = [-2,-5,-98,-46,-3,-21,-69,-98,-54,-31]
Solution().MS(a)
