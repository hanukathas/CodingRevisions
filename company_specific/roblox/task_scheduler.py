def task_scheduler(tasks: list, n: int):
    freq = [0] * 26
    for task in tasks:
        freq[ord(task) - ord('A')] += 1
    freq.sort()
    print(freq)
    chunk = freq[25] - 1 #fill in if there is only one task
    print(chunk)
    idle = chunk * n #idle if there is only one task
    print(idle)
    for i in range(24, -1, -1):
        idle -= min(chunk, freq[i])
        print(idle)

    return len(tasks) + idle if idle >= 0 else len(tasks)

if __name__ == '__main__':
    # print(task_scheduler(["A","A","A","B","B","B"], n = 2))
    # print(task_scheduler(["A","C","A","B","D","B"], n=1))
    print(task_scheduler(["A","A","A", "B","B","B"], n=3))
