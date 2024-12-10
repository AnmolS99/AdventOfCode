import math

file = open('2/input.txt', 'r')

def is_safe(nums):
    order = math.copysign(1, nums[1] - nums[0])
    prev_num = nums[0]
    
    for num in nums[1:]:

        if order == 1:
            if num - prev_num > 3 or num - prev_num < 1:
                return False
        
        else:
            if prev_num - num > 3 or prev_num - num < 1:
                return False
        
        prev_num = num
    
    return True

num_safe_reports = 0

for report in file.readlines():    
    data = report.strip()
    nums = list(map(int, data.split()))
    if is_safe(nums):
        num_safe_reports += 1

print(num_safe_reports)