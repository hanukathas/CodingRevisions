from graphs.connected_components import connected_components

parent = []
def find(x):
    if parent[x] == x:
        return x
    rootx = find(parent[x])
    parent[x] = rootx
    return rootx
size = []
components = 0 # number of connected components set
def union(u, v, components=None):
    rootu = find(u)
    rootv = find(v)
    if size[rootu] < size[rootv]:
        size[rootv] += size[rootu]
        parent[rootu] = rootv
    else:
        size[rootu] += size[rootv]
        parent[rootv] = rootu
    
    # reduce distinct connected components
    components -= 1
