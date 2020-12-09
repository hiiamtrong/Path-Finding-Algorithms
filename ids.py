
def IDS(tree, root, goals, maxDepth):
    # init list of nodes was visted
    visted = dict()
    # init list of node with it's level
    children = dict()
    # init list of nodes will be passed througt, start with head node
    opens = list(root)
    # init list of nodes was has been passed
    closed = list()
    children[root] = {"level": 0, "node": root}
    isDone = False
    while not isDone:
        if len(opens) <= 0:
            break
        # current node
        node = opens[0]
        closed.append(node)
        if(visted.get(node, False) == True):
            break
        else:
            visted[node] = True
        if(node in goals):
            isDone = True
            break
        childNodes = tree.get(node)
        currentDepth = children[node]["level"]
        opens.pop(0)
        if not childNodes:
            continue
        if currentDepth == 0 or currentDepth % maxDepth != 0:
            opens[:0] = childNodes
        else:
            opens.extend(childNodes)
        for childNode in childNodes:
            children[childNode] = {
               "level": currentDepth+1, "node": childNode
            }

    print('\nIDS')
    if(isDone):
        print(' => '.join(closed))
    else:
        print(f'Not found [{", ".join(goals)}] in this tree')
