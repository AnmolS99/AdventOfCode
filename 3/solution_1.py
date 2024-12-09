import re

def calculate_product(mul_string: str):
    num1, num2 = mul_string[4:-1].split(',')
    print(f"{num1} {num2}")
    return int(num1)*int(num2)

pattern = r'mul\(\d+,\d+\)'

with open("input.txt", "r") as f:
    
    mul_sum = 0
    
    for line in f.readlines():

        matches = re.findall(pattern, line)
        
        
        for match in matches:
            mul_sum += calculate_product(match)
    
    print(mul_sum)