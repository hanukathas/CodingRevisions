def balloon_bursts(points: list):
    """
    https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
    :param points:
    :return:
    """
    points.sort(key=lambda item: item[1])
    num_arrows = 1
    cur_end = points[0][1]

    for i in range(1, len(points)):
        if cur_end < points[i][0]:
            num_arrows += 1
            cur_end = points[i][1]
    return num_arrows

def balloon_bursts_r(points: list):
    points.sort(key= lambda items: (items[0], -items[1]))
    arrows = 1
    curr = points[0]

    for point in points:
        if curr[1] < point[0]:
            curr[1] = point[1]
            arrows += 1
    return arrows


if __name__ == '__main__':
    print(balloon_bursts_r([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(balloon_bursts_r([[1,2], [3,4], [5,6]]))
