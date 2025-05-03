from collections import deque

q = deque()
indegree = []
dependents = []

def can_be_completed(n: int, a: list, b: list):
    """
    https://leetcode.com/problems/course-schedule/description/
    Kahns's algorithm:
    maintain the following arrays:
    1. indegree: dependents count of courses, for a given course
    2. dependentss: a matrix of dependents courses
    3. queue: completed courses

    n total courses
    a courses
    b dependents courses
    :param n:
    :param a:
    :param b:
    :return:
    """
    global indegree, dependents
    indegree = [0] * n
    dependents = [[] for _ in range(n)]

    # set the dependency count in indegree and courses in dependents
    for i in range(len(a)):
        # Counting the number of prerequisite courses for course[b[i]] which are yet
        # to be completed.
        indegree[b[i]] += 1

        # listing the dependents of every course.
        dependents[a[i]].append(b[i])

    # for courses that have no dependents, complete them
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    # check for courses that could not be completed after traversal.
    # if all courses in indegree is not 0, then dependency courses are not completed
    # cannot graduate, return false

    while q:
        course = q.popleft()  # Complete the course.

        for d in dependents[course]:
            # Decreasing the number of prerequisite courses for course[b[i]] which are yet
            # to be completed.
            print(d)
            indegree[d] -= 1

            # Has no prerequisite courses, so can be completed now.
            if indegree[d] == 0:
                q.append(d)


    for i in range(n):
        if indegree[i] != 0:
            return False
    # above loop would have returned false if the course dependencies were not completed
    return True
