
left = []
right = []
with open("1/input.txt", "r") as f:
    while True:
        nums = f.readline().split()
        if not nums:
            break
        left.append(int(nums[0]))
        right.append(int(nums[1]))

left_sorted = sorted(left)
right_sorted = sorted(right)

sum_dist = 0
for i in range(len(left)):
    sum_dist += abs(left_sorted[i] - right_sorted[i])

print(sum_dist)
    
