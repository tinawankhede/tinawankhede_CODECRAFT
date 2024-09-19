
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set() 
        
    
    visited.add(start)
    
   
    
   
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            

if _name_ == "_main_":
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
   
    print("Depth-First Search starting from vertex A:")
    dfs(graph, 'A')