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
# list of goals of DFS, DFS, IDS algorithms
goals = dataJson['goals']

hill_climb = dataJson['hill-climb']
# list of goals of HC algorithm
goals_HC = dataJson['hill-climb']['goals']
# root node
root = dataJson['root']

if __name__ == '__main__':
    DFS(tree, root, goals)
    BFS(tree, root, goals)
    IDS(tree, root, goals, 2)
    HC(hill_climb, root, goals_HC)
