with open("7/input.txt", "r") as f:
    content = f.read()

    equations = [line for line in content.split("\n") if line.strip()]

def can_equation_be_true(answer, values):
    
    if len(values) == 1:
        if values[0] == answer:
            return True
        return False
    
    left_elems_sum = (values[0] + values[1])
    
    left_elems_product = (values[0] * values[1])

    left_elems_concat = int(str(values[0]) + str(values[1]))

    if len(values) == 2:
        return can_equation_be_true(answer, [left_elems_sum]) or can_equation_be_true(answer, [left_elems_product]) or can_equation_be_true(answer, [left_elems_concat])
    
    return can_equation_be_true(answer, [left_elems_sum] + values[2:]) or can_equation_be_true(answer, [left_elems_product] + values[2:]) or can_equation_be_true(answer, [left_elems_concat] + values[2:])

equation_sum = 0

for equation in equations:
    answer, values = equation.split(':')
    answer = int(answer)
    values = [int(value) for value in values.split(" ") if value]
    if can_equation_be_true(answer, values):
        equation_sum += answer

print(equation_sum)