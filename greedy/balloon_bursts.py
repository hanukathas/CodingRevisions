def balloon_bursts(points: list):
    """
    https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
    :param points:
    :return:
    """
    points.sort(key= lambda item: item[1])
    num_arrows = 1
    cur_end = points[0][1]

    for i in range(1, len(points)):
        if cur_end < points[i][0]:
            num_arrows += 1
            cur_end = points[i][i]
    return num_arrows

if __name__ == '__main__':
    print(balloon_bursts([[10,16],[2,8],[1,6],[7,12]]))