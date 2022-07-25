

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = {}

def indegree(graph):
    indegree_dict = {}
    
    for k in graph.keys():
        indegree_dict[k] = 0
        visited[k] = False
    
    for adjlist in graph.values():
        for n in adjlist:
            indegree_dict[n] += 1
            
    return indegree_dict
    
def alltopologicalSort(graph,indegree, path):

    for v in graph.keys():
        if indegree[v] == 0 and not visited[v]:
            
            for adj in graph[v]:
                indegree[adj] -= 1
                
            path.append(v)
            visited[v] = True
            
            alltopologicalSort(graph,indegree,path)
            
            for adj in graph[v]:
                indegree[adj] += 1
                
            path.pop()
            visited[v] = False
            
    if len(path) == len(graph.keys()):
        print (path)
        
ind = indegree(graph)
alltopologicalSort(graph,ind,[])
            