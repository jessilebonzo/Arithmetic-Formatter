def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    top_line = ""
    bottom_line = ""
    dashes_line = ""
    result_line = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2

        top_line += operand1.rjust(width) + "    "
        bottom_line += operator + operand2.rjust(width - 1) + "    "
        dashes_line += "-" * width + "    "

        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            result_line += result.rjust(width) + "    "

    arranged_problems += top_line.rstrip() + "\n"
    arranged_problems += bottom_line.rstrip() + "\n"
    arranged_problems += dashes_line.rstrip()

    if show_answers:
        arranged_problems += "\n" + result_line.rstrip()

    return arranged_problems

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
