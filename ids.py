
def IDS(tree, root, goal, maxDepth):
    # init some variable to save some useful infomation
    visted = dict()
    closed = dict()
    opens = list(root)
    result = list()
    closed[root] = {"visted": True, "level": 0, "node": root}
    isDone = False
    while not isDone:
        if len(opens) <= 0:
            break
        node = opens[0]
        result.append(node)
        if(visted.get(node, False) == True):
            break
        else:
            visted[node] = True
        if(node == goal):
            isDone = True
            break
        childNodes = tree.get(node)
        currentDepth = closed[node]["level"]
        opens.pop(0)
        if not childNodes:
            continue
        if currentDepth == 0 or currentDepth % maxDepth != 0:
            opens[:0] = childNodes
        else:
            opens.extend(childNodes)
        for childNode in childNodes:
            closed[childNode] = {
                "visted": True, "level": currentDepth+1, "node": childNode
            }

    print('\nIDS')
    if(isDone):
        print(' => '.join(result))
    else:
        print(f'Not found {goal} in this tree')
