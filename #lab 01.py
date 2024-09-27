#lab 01
#Dynamic calculator ( solving : 1+2×3(4-5÷4)-(3÷5) )


def calculate(expression):
    try:
        # Replace '×' with '*' for multiplication and '÷' with '/' for division
        expression = expression.replace('×', '*').replace('÷', '/')
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

# Example:
expression = "1 + 2 * 3 * (4 - 5 / 4) - (3 / 5)"
print(calculate(expression))
