import sys
sys.setrecursionlimit(10**5+5)
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
 
    def DFSUtil(self, temp, v, visited):
 # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp
 
    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
 
    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
 
 
# Driver Code
if __name__ == "__main__":
 
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    nodes=int(input())
    g = Graph(nodes)
    #print(g)
    l=list(map(int,input().split(" ")))
    edges=int(input())
    for _ in range(edges):
        a,b=map(int,input().split(" "))
        g.addEdge(a-1,b-1)
    
    cc = g.connectedComponents()
    #print("Following are connected components")

    #print(cc)
    summ=[]
    for i in range(len(cc)):
        addition=0
        for j in range(len(cc[i])):
            addition+=l[cc[i][j]]
        summ.append(addition)
    y=max(summ)
    if summ.count(y)==1:
        indexx=summ.index(y)
        answer=cc[indexx]
        final=[]
        for each in answer:
            each+=1
            final.append(each)
        final.sort()
        for x in final:
            print(x,end=" ")
    else:
        aa=[]
        for i in range(len(summ)):
            if summ[i]==y:
                indexx=i
                aa.append(cc[indexx])
        answer=max((x) for x in aa)
        final=[]
        for each in answer:
            each+=1
            final.append(each)
        final.sort()
        for x in final:
            print(x,end=" ")
        





     