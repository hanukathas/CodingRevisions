import heapq


def min_spannng_tree(n: int, matrix: list):
    pass

def min_spanning_tree_kruskal(n: int, matrix: list):
    """
    company_specific: https://leetcode.com/problems/connecting-cities-with-minimum-cost/description/?envType=problem-list-v2&envId=minimum-spanning-tree
    proof by contradiction:
    -> another spanning tree that is constructed is minimum spanning tree
    if weights till edge i - 1 matches and does not match for edge i
    for edge i pick wi1, and another exists wi2.
    there must be reason why wi1 was picked wi2:
        a. wi1 does not create cycle. if the cycle for wi2 is removed, wi1 wins
        b. wi1 is lesser than wi2
    so,
    1. focus on subtrees. if a subtree is minimum span, then it contributes to the overall tree
    2. so union of minimum subtrees gives the minimum span tree
    3. note: the weights choses cannot create cycles
    :param n:
    :param matrix:
    :return:
    """
    # implement union find
    size = [1 for _ in range(n)]
    parent = [i for i in range(n)]
    components = n  # no vertex is connected
    total_cost = 0
    result = []
    sorted(matrix, key=lambda items: items[2])

    def find(x: int):
        if x == parent[x]:
            return x
        else:
            rootx = find(parent[x])
            parent[x] = rootx
            return rootx

    for u, v, w in matrix:
        rootu = find(u)
        rootv = find(v)
        if size[rootu] < size[v]:
            parent[rootu] = rootv
            size[rootv] += size[rootu]
        else:
            parent[rootv] = rootu
            size[rootu] += size[rootv]
        components -= 1
        total_cost += w
        result.append((u,v))
    if components == 1:
        return total_cost
    else:
        return -1

def min_spanning_tree_prim(n: int, matrix: list):
    """

    1. build the adjacency list
    2. set up captured list and set captured of origin to True
    :param n:
    :param matrix:
    :return:
    """
    adj_list = [] * n
    for u,v,w in matrix:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    captured = [False] * n
    captured[0] = True
    pq = []
    total_cost = 0
    for u,w in adj_list[0]:
        heapq.heappush(pq, (u,w))

    while pq:
        vertex, weight = pq.heappop()
        if captured[vertex]:
            continue
        captured[vertex] = True
        total_cost += weight
        for neighbor, cost in adj_list[vertex]:
           if not captured[neighbor]:
               heapq.heappush(pq, (neighbor, cost))
               captured[neighbor] = True

    return total_cost











