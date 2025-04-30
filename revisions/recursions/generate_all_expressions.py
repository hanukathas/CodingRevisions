def generate_expressions(s, target):
    def recurse(index, curr_value, curr_expr):
        # Base case: reached end of string
        if index == len(s):
            if curr_value == target:
                result.append(curr_expr)
            return

        # Get all possible numbers starting from current index
        for i in range(index, len(s)):
            # Handle numbers with leading zeros correctly
            curr_num = s[index:i + 1]
            num = int(curr_num)

            # If it's the first number, no operator needed

            if index == 0:
                recurse(i + 1, num, curr_num)
            else:
                # Try addition
                recurse(i + 1, curr_value + num, curr_expr + '+' + curr_num)
                # Try multiplication
                if curr_expr[-1] != '0':
                    recurse(i + 1, curr_value * num, curr_expr + '*' + curr_num)

    result = []
    recurse(0, 0, '')
    return result


def generate_expressions_r(num: [], target: int):
    if len(num) == 1 and num[0] == target:
        return str(num[0])
    result = []
    def helper(index, sum, expression):

        if index == len(num):

            if sum == target:
                result.append(expression)
            sum = 0
            expression = ""
            return

        for i in range(index, len(num)):
            cur_num = num[index:i + 1]
            cur_val = int(cur_num)

            if index == 0:
                helper(i + 1, cur_val, cur_num)
            else:
                helper(i + 1, sum + cur_val, expression + "+" + cur_num)
                if expression[-1] != 0:
                    helper(i + 1, sum * cur_val, expression + "*" + cur_num)

    helper(0, 0, "")

    return result


if __name__ == '__main__':
    s = "232"
    target = 8
    print(generate_expressions(s, target))  # ['1*2*3', '1+2+3']
    print(generate_expressions_r(s, target))  # ['1*2*3', '1+2+3']
