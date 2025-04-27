def min_arrows(points: list):
    """
    https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
    :param points:
    :return:
    """
    points.sort(key=lambda item: item[1])

    min_arrows_required = 1
    point_end = points[0][1]
    for i in range(1, len(points)):
        if point_end < points[i][0]:
            min_arrows_required += 1
            point_end = points[i][1]
    return min_arrows_required

def min_arrows_r(points: list):
    arrows = 1
    sorted_points = sorted(points, key=lambda items: items[1])
    cur_end_point = sorted_points[0][1]
    for i in range(1, len(sorted_points)):
        if cur_end_point < sorted_points[i][0]:
            arrows += 1
            cur_end_point = sorted_points[i][1]
    return arrows


if __name__ == '__main__':
    print(min_arrows([[10,16], [2,8], [1,6], [7,12]]))
    print(min_arrows([[1,2],[3,4],[5,6],[7,8]]))

    print(min_arrows_r([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(min_arrows_r([[1, 2], [3, 4], [5, 6], [7, 8]]))
