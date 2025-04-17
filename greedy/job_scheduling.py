def job_scheduling(jobs: list):
    jobs.sort()
    total_spent = 0

    for i in range(len(jobs)):
        total_spent += jobs[i]
    return total_spent

if __name__ == '__main__':
    points = [[10,16], [2,8], [1,6], [7,12]]

    points.sort(key= lambda item:(item[0], -item[1]))

    print(points)
    max_arrows = {0: 1}














