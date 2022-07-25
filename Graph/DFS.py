
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

def dfs(graph,node):
    visited.append(node)
    stack.append(node)
    
    while len(stack) > 0:
        v = stack.pop()
        
        print (v)
        
        for adjnode in graph[v]:
            if not adjnode in visited:
                visited.append(adjnode)
                stack.append(adjnode)
            
dfs(graph,'5')