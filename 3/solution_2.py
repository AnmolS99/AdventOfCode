import re

def calculate_product(mul_string: str):
    num1, num2 = mul_string[4:-1].split(',')
    print(f"{num1} {num2}")
    return int(num1)*int(num2)

mul_pattern = r'mul\(\d+,\d+\)'

meta_pattern = r'^(.*?)don\'t\(\)|do\(\)(.*?)don\'t\(\)|do\(\)(.*?)$'

with open("input.txt", "r") as f:
    
    content = f.read()
    mul_sum = 0

    enabled_substrings = re.findall(meta_pattern, content)
    print(enabled_substrings)

    for substring in enabled_substrings:

        combined_substring = ''.join(filter(None, substring))

        matches = re.findall(mul_pattern, combined_substring)
            
        for match in matches:
            mul_sum += calculate_product(match)
    
    print(mul_sum)