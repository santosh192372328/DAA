#Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k
nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
n=len(nums)
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] == nums[j] and (i * j) % k == 0:
            count += 1
print(count)  

# Output: 4
