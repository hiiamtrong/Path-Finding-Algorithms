def HC(Graph, head, goals):
    graph = Graph['graph']
    h = Graph['h']
    # init list of nodes was visted
    visted = dict()
    # init list of nodes was has been passed
    closed = []
    # init list of nodes will be passed througt, start with head node
    opens = list(head)
    isDone = False
    while not isDone:
        childNodes_with_h = {}
        if len(opens) <= 0:
            break
        # current node
        node = opens[0]
        closed.append(f'{node}({h[node]})')

        if visted.get(node, False) == True:
            break
        else:
            visted[node] = True
        if(node in goals):
            isDone = True
            break
        opens.pop(0)
        childNodes = graph.get(node)
        if(childNodes):
            for childNode in childNodes:
                childNodes_with_h[childNode] = h.get(childNode)
            sorted_dict = dict(
                sorted(childNodes_with_h.items(), key=lambda k: k[1]))
            # push childNodes to head of opens
            opens[:0] = sorted_dict.keys()
    print('\nHC')
    if(isDone):
        print(" => ".join(closed))
    else:
        print(f'Not found [{", ".join(goals)}] in this tree')
