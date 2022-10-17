

from collections import defaultdict

class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph

        self.total_scc = 0

        self.new_list = []




    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
  




    # A function used by DFS
    def DFSUtil(self,v,visited):
        # Mark the current node as visited and print it
        visited[v]= True
        print(v, end=',', file=open("output.txt", 'a')),
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
    
    def my_dfs(self, v, visited):
        visited[v] = True 
        print(v)
        self.new_list.append(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.my_dfs(i, visited)
                
 
 
    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
     
 
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
 
  
  
    # The main function that finds and prints all strongly
    # connected components

    def main_scc(self):

        self.final_list = []

        stack = []
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        
        gr = self.getTranspose()

        visited = [False] * (self.V)

        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.my_dfs(i, visited)
                self.new_list.append(',')
                

                self.total_scc += 1



    def printSCCs(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
 
        # Create a reversed graph
        gr = self.getTranspose()
          
         # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)
 
         # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSUtil(i, visited)
                #print("")
                print(" ", file=open("output.txt", 'a'))
                self.total_scc += 1


list1 = []

go = True

while go == True:
    mine = input()
    list1.append(mine)
    if mine =='stop':
        break


nodes = int(list1[0])
edges = int(list1[1])
g = Graph(nodes)

edges_list = []
for i in list1[2:-1]:
    edges_list.append((int(i[0]), int(i[2])))
    g.addEdge(int(i[0]), int(i[2]))


g.printSCCs()

with open('output.txt', 'r') as f:
    contents = f.readlines()

new_list = []
for i in contents:
    new_list.append(i.strip())

connected = len(new_list)


#print("The graph has {} strongly connected componets".format(len(new_list)))
for i,n  in enumerate(new_list, 1):
    print("strongly connected component #{} is {}".format(i, n), file=open("new_output.txt", 'a'))


with open("new_output.txt", 'r') as f:
    final_contents = f.readlines()

print("The graph has {} strongly connected components".format(len(new_list)))
for i in final_contents:
    print(i)