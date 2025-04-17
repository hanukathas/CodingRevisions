def min_arrows(points: list):
    points.sort(key=lambda item: item[1])

    min_arrows_required = 1
    point_end = points[0][1]
    for i in range(1, len(points)):
        if point_end < points[i][0]:
            min_arrows_required += 1
            point_end = points[i][1]
    return min_arrows_required

if __name__ == '__main__':
    print(min_arrows([[10,16], [2,8], [1,6], [7,12]]))
    print(min_arrows([[1,2],[3,4],[5,6],[7,8]]))
