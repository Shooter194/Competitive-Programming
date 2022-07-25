
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []

def bfs(graph,node):
    visited.append(node)
    queue.append(node)
    
    while len(queue) > 0:
        vertex = queue.pop(0)
        print (vertex)
        for adjnode in graph[vertex]:
            if not adjnode in visited:
                queue.append(adjnode)
                visited.append(adjnode)
                
bfs(graph,'5')