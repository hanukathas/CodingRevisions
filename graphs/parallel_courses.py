def parallel_courses(matrix: list, n: int):
    """
    https://leetcode.com/problems/parallel-courses/description/
    """
    adjacency_list = [[] for _ in range(n+1)]
    for src, dst in matrix:
        adjacency_list[src].append(dst)

    visited = [False] * (n + 1)
    departure = [-1] * (n + 1)
    timestamp = [0]
    topsort = []

    def dfs(origin: int):
        """
        I can keep learning and create a topological sort as long as I don't detect a cycle
        how do I detect a cycle?
        when departure of the node is complete but only visited
        :param origin:
        :return:
        """
        visited[origin] = True
        for vertex in adjacency_list[origin]:
            if visited[vertex] is False:
                if dfs(vertex):
                    return True
            else:
                if departure[vertex] == -1: # hit the vertex again
                    return True
            # all vertexes from this origin is visited and no cycles found
            # I depart now

        departure[origin] = timestamp[0]
        timestamp[0] += 1
        # add to the topsort
        topsort.append(origin)
        print(topsort)
        return False

    # build the topological array using DFS. return -1 if a cycle is found
    for vertex in range(n):
        if not visited[vertex]:
            if dfs(vertex):
                print(topsort)
                return -1

    # now reverse the topological graph as the vertices are in the decreasing order of departutre times
    topsort.reverse()

    # we will do DP. but this one is not straightforward.
    # we will compute the longest part from the start vertex to the last vertex.
    # the longest path is the answer

    # base case: "even for origin we start from somewhere" so our table will have size n+1
    table = [1] * (n+1)

    for vertex in topsort:
        for neighbor in adjacency_list[vertex]:

            table[neighbor] = max(table[neighbor], 1 + table[vertex])

    return max(table)


if __name__ == '__main__':
    print(parallel_courses([[1,3],[2,3]], 3))