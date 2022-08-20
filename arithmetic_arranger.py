import re
import operator


def isvalid(problems):
    valid = True
    message = ""
    while valid is not False:

        # check if there are more than 5 problems
        if len(problems) > 5:
            valid = False
            message = "Error: Too many problems."
            break

        # check if each operand only contains digits
        try:
            for element in problems:
                try:
                    element = re.findall("[^ 0-9]", element)
                    if len(element) > 1:
                        message = "Error: Numbers must only contain digits."
                        valid = False
                        break
                except:
                    pass
        except:
            message = "Error: Numbers must only contain digits."
            valid = False
            break

        # check if the operator is + or -
        for element in problems:
            try:
                match_check = re.search("([ ]*)([0-9]+)([ ]*)+(.)([ ]*)([0-9]+)([ ]*)", element)
                if match_check.group(4) not in ["+", "-"]:
                    message = "Error: Operator must be '+' or '-'."
                    break
            except:
                pass

        # check if the operands are more than four digits
        for element in problems:
            element = re.findall("[0-9]+",element)
            for number in element:
                if len(number) > 4:
                    valid = False
                    message = "Error: Numbers cannot be more than four digits."
        break
    return message

def arithmetic_arranger(problems, result=False):

    # lists to be populated by the append method
    number1s = []
    number2s = []
    operators = []
    to_be_printed = []
    my_string = isvalid(problems)
    # check if user input is valid
    if my_string == "":

        # returns all elements from the problem, grouped
        # for example, "22+ 55" each operand and operator can be accesed using the 'group' function from the regex library
        for i in range(len(problems)):
            match_check = re.search("([ ]*)([0-9]+)([ ]*)+([+]|-)([ ]*)([0-9]+)([ ]*)",
                                    problems[i])
            number1s.append(match_check.group(2))
            number2s.append(match_check.group(6))
            operators.append(match_check.group(4))

        # prints the above operands
        for i in range(len(number1s)):
            spaces = (len(str(abs(max(int(number1s[i]), int(number2s[i])))))+2)
            if i != (len(number1s) - 1):
                to_be_printed.extend(f"{number1s[i]:>{spaces}}" + "    ")
            else:
                to_be_printed.extend(f"{number1s[i]:>{spaces}}" + "")
        to_be_printed.extend("\n" + "")  # prints new line

        # prints the operator and the below operands
        for i in range(len(number1s)):
            spaces = (len(str(abs(max(int(number1s[i]), int(number2s[i])))))+1)
            if i != (len(number1s) - 1):
                to_be_printed.extend(operators[i]+f"{number2s[i]:>{spaces}}" + "    ")
            else:
                to_be_printed.extend(operators[i]+f"{number2s[i]:>{spaces}}" + "")
        to_be_printed.extend("\n" + "")  # prints new line

        # prints the dashes based on result length
        for i in range(len(number1s)):
            dashes = "-" * (len(str(abs(max(int(number1s[i]), int(number2s[i])))))+2)
            if i != (len(number1s) - 1):
                to_be_printed.extend(dashes + "    ")
            else:
                to_be_printed.extend(dashes + "")

        # prints the result if user input is True
        if result:
            to_be_printed.extend("\n" + "")  # prints new line
            for i in range(len(number1s)):
                ops = {"+": operator.add, "-": operator.sub}  # create lookup table for the operators
                resulted = ops[operators[i]](int(number1s[i]), int(number2s[i]))  # arithmetic result
                spaces = (len(str(abs(max(int(number1s[i]), int(number2s[i])))))+2)
                if i != (len(number1s) - 1):
                    to_be_printed.extend(f"{resulted:>{spaces}}" + "    ")  # printing the results
                else:
                    to_be_printed.extend(f"{resulted:>{spaces}}" + "")  # printing the results without spaces at the end for the final problem
        for element in to_be_printed:
            my_string += element
    return my_string
