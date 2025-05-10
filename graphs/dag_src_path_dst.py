def dag_src_path_dst(graph: list):
    m = len(graph)
    n = len(graph[0])

    result = []
    def helper(vertex, slate: list):
        if vertex == n-1:
            slate.append(vertex)
            result.append(slate[:])
            slate.pop()
            return
        else:
            slate.append(vertex)
            for vert in graph[vertex]:
                helper(vert, slate)
            slate.pop()
    helper(0, [])
    return result

def dag_src_path_dst_r(graph: list):
    m = len(graph)
    n = len(graph[0])

    result = []
    def helper(vertex, slate):
        if vertex == n - 1:
            slate.append(vertex)
            result.append(slate[:])
            slate.pop()
        else:
            slate.append(vertex)
            for vert in graph[vertex]:
                helper(vert, slate)
            slate.pop()
    helper(0, [])
    return result