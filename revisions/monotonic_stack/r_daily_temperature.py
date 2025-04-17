def r_daily_temperature(temperatures: list):
    span = []
    r_daily_temperature_stack = []

    for i in range(len(temperatures)-1, -1, -1):
        while r_daily_temperature_stack and r_daily_temperature_stack[-1][0] <= temperatures[i]:
            r_daily_temperature_stack.pop()

        if r_daily_temperature_stack:
            span.append(r_daily_temperature_stack[-1][1] - i)
        else:
            span.append(0)
        r_daily_temperature_stack.append((temperatures[i], i))

    return span

if __name__ == '__main__':
    print(r_daily_temperature([30, 40, 50, 60]))
    print(r_daily_temperature([30, 50, 60, 40]))
    print(r_daily_temperature([80, 50, 40, 60]))
