class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        disc = [-1]*n
        low = [-1]*n
        self.time = 0
        graph = defaultdict(list)
        bridges = []
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node,parent):
            #print(parent)
            if disc[node] != -1:
                return 
            
            disc[node] = self.time
            low[node] = self.time
            self.time += 1
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor,node)
                
                low[node] = min(low[neighbor],low[node])
                
                if disc[node] < low[neighbor] :
                    bridges.append([node,neighbor])
                    
        dfs(0,-1)
        #print(low)
        return bridges