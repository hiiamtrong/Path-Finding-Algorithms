
def DFS(tree, root, goal):
    visted = dict()
    opens = [root]
    result = list()
    isDone = False
    while not isDone:
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
        childNode = tree.get(node)
        if(childNode):
            opens[:0] = childNode
    print('\nDFS')
    rs = ' => '.join(result)
    if(isDone):
        print(' => '.join(result))
    else:
        print(f'Not found {goal} in this tree')
