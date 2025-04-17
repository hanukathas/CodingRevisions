def balloon_bursts(points: list):
    points.sort(key= lambda item: item[1])
    num_arrows = 1
    cur_end = points[0][1]

    for i in range(1, len(points)):
        if cur_end < points[i][0]:
            num_arrows += 1
            cur_end = points[i][i]
    return num_arrows
