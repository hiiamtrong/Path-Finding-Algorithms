
def BFS(tree, root, goal):
    # init list of nodes was visted
    visted = dict()
    # init list of nodes will be passed througt, start with head node
    opens = [root]
    # init list of nodes was has been passed
    closed = list()
    isDone = False
    while not isDone:
        if len(opens) <= 0:
            break
        node = opens[0]
        closed.append(node)
        if visted.get(node, False) == True:
            break
        else:
            visted[node] = True
        if(node == goal):
            isDone = True
            break
        opens.pop(0)
        childNodes = tree.get(node)
        if(childNodes):
            opens.extend(childNodes)
    print('\nBFS')
    if(isDone):
        print(' => '.join(closed))
    else:
        print(f'Not found {goal} in this tree')
