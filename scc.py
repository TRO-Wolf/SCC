

from collections import defaultdict

class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices

        # a default dictionary which will act as an adjacency list
        self.graph = defaultdict(list) 

        self.total_scc = 0

        self.new_list = []





    
    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
  




    
    def dfs(self, v, visited_bool):
        # Mark the current node as visited and print it
        visited_bool[v] = True

        print(v, end=',', file=open("output.txt", 'a')),
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited_bool[i]==False:
                self.dfs(i, visited_bool)

    

                
 
 


    
    def mark_node(self, v, visited_bool, stack):
        # Mark the current node as visited
        visited_bool[v] = True
        #Recure for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited_bool[i]==False:
                self.mark_node(i, visited_bool, stack)
        stack = stack.append(v)

    

     
 


    # Function that returns reverse (or transpose) of this graph
    def reverse_graph(self):

        g = Graph(self.V)
        # Recure for all the vertices adjacent to this vertex
        for i in self.graph:
            for n in self.graph[i]:
                g.add_edge(n, i)
        return g
 
  
  
    # The main function that finds and prints all strongly
    # connected components




    
    def get_scc(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited_bool = [False]* (self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited_bool[i]==False:
                self.mark_node(i, visited_bool, stack)

        # Create a reversed graph
        new_graph = self.reverse_graph()

        # Mark all the vertices as not visited (For second DFS)
        visited_bool = [False]*(self.V)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited_bool[i]==False:
                new_graph.dfs(i, visited_bool)
                print(" ", file=open("output.txt", 'a'))
                self.total_scc += 1



#list to keep the inputs from stdin
list1 = []

go = True
print("start typing your inputs")
while go == True:
    mine = input()
    list1.append(mine)
    if mine =='stop':
        break


nodes = int(list1[0])
edges = int(list1[1])
g = Graph(nodes)

#code to add each edge from the stdin into the graph
edges_list = []
for i in list1[2:-1]:
    edges_list.append((int(i[0]), int(i[2])))
    g.add_edge(int(i[0]), int(i[2]))


#this is where the algorithm is ran

g.get_scc()

#this is a method to print the strongly connected components to a new file
with open('output.txt', 'r') as f:
    contents = f.readlines()


new_list = []
for i in contents:
    new_list.append(i.strip())

connected = len(new_list)



for i,n  in enumerate(new_list, 1):
    print("strongly connected component #{} is {}".format(i, n), file=open("new_output.txt", 'a'))


with open("new_output.txt", 'r') as f:
    final_contents = f.readlines()

print("The graph has {} strongly connected components".format(len(new_list)))
for i in final_contents:
    print(i)