def non_overlapping_scheduling(schedules: list):
    """
    option 1: pick the activity that overlaps with few other activities
    option 2: order by end times -> yields optimal solution
    :param schedules:
    :return:
    """
    schedules.sort(key= lambda item: item[1])

    non_overlapping = 1
    last_meeting_end = schedules[0][1]
    for i in range(1, len(schedules)):
        if last_meeting_end <= schedules[i][0]:
            non_overlapping += 1
            last_meeting_end = schedules[i][1]

    return non_overlapping






