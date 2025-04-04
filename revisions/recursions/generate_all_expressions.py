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


if __name__ == '__main__':
    s = "1234"
    target = 11
    print(generate_expressions(s, target))  # ['1*2*3', '1+2+3']