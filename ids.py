
def IDS(tree, root, goal, maxDepth):
    # init some variable to save some useful infomation
    visted = dict()
    children = dict()
    opens = list(root)
    closed = list()
    children[root] = {"visted": True, "level": 0, "node": root}
    isDone = False
    while not isDone:
        if len(opens) <= 0:
            break
        node = opens[0]
        closed.append(node)
        if(visted.get(node, False) == True):
            break
        else:
            visted[node] = True
        if(node == goal):
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
                "visted": True, "level": currentDepth+1, "node": childNode
            }

    print('\nIDS')
    if(isDone):
        print(' => '.join(closed))
    else:
        print(f'Not found {goal} in this tree')
