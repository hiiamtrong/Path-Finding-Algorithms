from json import loads
from bfs import BFS
from dfs import DFS
from ids import IDS
from hc import HC

# Load tree data from file
filePath = open('./data.json')
data = filePath.read()
dataJson = loads(data)
tree = dataJson['tree']
hill_climb = dataJson['hill-climb']


if __name__ == '__main__':
    DFS(tree, 'S', 'F')
    BFS(tree, 'S', 'F')
    IDS(tree, 'S', 'F', 2)
    HC(hill_climb, 'A', 'B')
