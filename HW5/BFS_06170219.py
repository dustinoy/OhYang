from collections import defaultdict 

class Graph: 
   
    def __init__(self): 
   
        self.graph = defaultdict(list) 
   
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    def BFS(self, s): 
   
        visited = [False] * (len(self.graph)) 
   
        queue = [] 
  
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            s = queue.pop(0) 
            print (s, end = " ") 
  
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
    def DFSUtil(self, s, visited): 
  
        
        visited[s] = True
        print(s, end = ' ') 
  
         
        for i in self.graph[s]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  
    def DFS(self, s): 
  
       
        visited = [False] * (len(self.graph)) 
  
     
        self.DFSUtil(s, visited)

      
## 參考資料(https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
##        (https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
