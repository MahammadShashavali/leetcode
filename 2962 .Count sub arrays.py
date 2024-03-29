class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxn=max(nums)
        i=s=maxl=0
        for end in range(len(nums)):
            if nums[end]==maxn:
                maxl+=1
            while maxl==k:
                if nums[s]==maxn:
                    maxl-=1
                s+=1
            i+=s
        return i
