
left = []
right = []
with open("1/input.txt", "r") as f:
    while True:
        nums = f.readline().split()
        if not nums:
            break
        left.append(int(nums[0]))
        right.append(int(nums[1]))

right_num_dict = {}

for num in right:
    if num not in right_num_dict:
        right_num_dict[num] = 1
    else:
        right_num_dict[num] += 1

sum_dist = 0
for num in left:
    if num in right_num_dict:
        sum_dist += num * right_num_dict[num]

print(sum_dist)
    
