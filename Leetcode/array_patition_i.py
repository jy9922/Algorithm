nums = [1, 4, 3, 2]

nums.sort()
result = 0

for i in range(0, len(nums), 2):
  result += min(nums[i], nums[i+1])

print(result)
    
  
