

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
stack = []

def topologicalSortUtil(graph,v):

    visited.append(v)
    if len(graph[v]) == 0 :
        stack.append(v)
        return
    
    
    for adjnode in graph[v]:
        if not adjnode in visited:
            topologicalSortUtil(graph,adjnode)
    stack.append(v)

def topologicalSort(graph):

    for v in graph.keys():
        if not v in visited:
            topologicalSortUtil(graph,v)
            
    print (stack[::-1])
    
topologicalSort(graph)