from collections import Counter
nums = [1,1,1,2,2,3]
k = 2

c_nums = list(Counter(nums).most_common(k))
print(list(c_nums[i][0] for i in range(len(c_nums))))

