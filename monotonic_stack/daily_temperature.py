def daily_temperature(temperatures: list):
    daily_temperature_stack = []
    answers = []
    for i in range(len(temperatures) - 1, -1, -1):
        while daily_temperature_stack and daily_temperature_stack[-1][0] <= temperatures[i]:
            daily_temperature_stack.pop()
        if daily_temperature_stack:
            answers.append(daily_temperature_stack[-1][1] - i)
        else:
            answers.append(0)

        daily_temperature_stack.append((temperatures[i], i))
    answers.reverse()
    return answers

if __name__ == '__main__':
    print(daily_temperature([30, 40, 50, 60]))
    print(daily_temperature([30, 50, 60, 40]))
    print(daily_temperature([80, 50, 40, 60]))
