class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:

    #base cases
    zero_count=0
    tot=1
    for e in nums:
      if e==0:zero_count+=1
      else:tot*=e
    
    if zero_count>1:
      for i in range(len(nums)):
        nums[i]=0
      return nums
    
    if zero_count==1:
      for i in range(len(nums)):
        if nums[i]==0: nums[i]=tot
        else:nums[i]=0
      return nums

    
    for i in range(len(nums)):
      nums[i]=tot//nums[i]

    return nums


    



"""



BRUTE FORCE

for i in range(arr)
  prod=1
  for j in range(arr):
    if i==j: continue

    prod*=arr[j]

  ans.append(prod)

return ans

if there are 2+ zeros all ans will be 0

if there are 1 zero answer is all 0 except the zero element


all non-zero

compute the product and for each element devide



"""