import re

def calculate_product(mul_string: str):
    num1, num2 = mul_string[4:-1].split(',')
    return int(num1)*int(num2)

mul_pattern = r'mul\(\d+,\d+\)'

with open("3/input.txt", "r") as f:
    
    content = f.read()
    mul_sum = 0

    enabled = True
    substring_start_idx = 0
    substring_end_idx = 0

    for i in range(len(content)):

        if i > 5 and enabled and content[i-6:i+1] == 'don\'t()':

            substring_end_idx = i

            matches = re.findall(mul_pattern, content[substring_start_idx : substring_end_idx + 1])
                
            for match in matches:
                mul_sum += calculate_product(match)
    
            enabled = False
        elif i > 2 and not enabled and content[i-3:i+1] == 'do()':
            
            substring_start_idx = i + 1

            enabled = True
    
    if enabled:
        
        matches = re.findall(mul_pattern, content[substring_start_idx:])
        
        for match in matches:
            mul_sum += calculate_product(match)
    

    print(mul_sum)