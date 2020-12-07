def HC(Graph, start, goal):
    graph = Graph['graph']
    h = Graph['h']
    visted = dict()
    result = []
    opens = list(start)
    isDone = False
    while not isDone:
        childNodes_with_h = {}
        if len(opens) <= 0:
            break
        node = opens[0]
        result.append(node)
        if visted.get(node, False) == True:
            break
        else:
            visted[node] = True
        if(node == goal):
            isDone = True
            break
        opens.pop(0)
        childNodes = graph.get(node)
        if(childNodes):
            for childNode in childNodes:
                childNodes_with_h[childNode] = h.get(childNode)
            sorted_dict = dict(
                sorted(childNodes_with_h.items(), key=lambda k: k[1]))
            opens[:0] = sorted_dict.keys()
    print('\nHC')
    if(isDone):
        for node in result:
            print(f"{node} ({h[node]})", end=' => ')
    else:
        print(f'Not found {goal} in this tree')
