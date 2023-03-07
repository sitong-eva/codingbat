"""

Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""

def sum2(nums):
    s=0
    if len(nums)==0:
        return 0
    if 0<len(nums)<2:
        s=sum(nums)
        return s
    if len(nums)>2:
        n=nums[0:2]
        #print(n)
        s=sum(n)
        #print(s)
        return s
    
print(sum2([1, 2, 3]))
