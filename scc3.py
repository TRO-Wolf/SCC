import os
from collections import defaultdict


if os.path.exists('new_output.txt'):
    os.remove('new_output.txt')

if os.path.exists('output.txt'):
    os.remove('output.txt')
    




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
print("start typing your inputs, when done finished type stop")
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



#this part reads the the data from contents and strips it of extra characters
#new_list contains the contents from the output.txt file
new_list = []
for i in contents:
    new_list.append(i.strip())


#this is an integer of the length of items found in the new_list
connected = len(new_list)


#loops through the new_list data and prints the contents to a new file called new_output.txt
for i,n  in enumerate(new_list, 0):
    print("strongly connected component #{} is {}".format(i, n), file=open("new_output.txt", 'a'))

#reads the contents from the new_output.txt file
with open("new_output.txt", 'r') as f:
    final_contents = f.readlines()

#converts the data from final contents
print("The graph has {} strongly connected components".format(len(new_list)))
print("")
for i in final_contents:
    print(i)





#class to run the KernalGraph
class KernalGraph:


    def __init__(self, components, contents, edge_data):
        
        #this reads the input from the contents data
        self.contents = contents

        #number of strongly connected components
        self.components = components

        #this is the data from the edges input 
        self.edges_list = edge_data
        self.node_list = []

        #this simply gets the nodes from the edges list and appends them to the nodes list
        for i in self.edges_list:
            self.node_list.append(i[0])

        #the total number of connected components, this portion reads the input from the self.contents attribute
        #
        if self.components == 8:
            self.c0 = self.conversion(node=0)
            self.c1 = self.conversion(node=1)
            self.c2 = self.conversion(node=2)
            self.c3 = self.conversion(node=3)
            self.c4 = self.conversion(node=4)
            self.c5 = self.conversion(node=5)
            self.c6 = self.conversion(node=6)
            self.c7 = self.conversion(node=7)
            self.scc_list = [self.c0, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7]
        elif self.components == 7:
            self.c0 = self.conversion(node=0)
            self.c1 = self.conversion(node=1)
            self.c2 = self.conversion(node=2)
            self.c3 = self.conversion(node=3)
            self.c4 = self.conversion(node=4)
            self.c5 = self.conversion(node=5)
            self.c6 = self.conversion(node=6)
            self.scc_list = [self.c0, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6]
        elif self.components == 6:
            self.c0 = self.conversion(node=0)
            self.c1 = self.conversion(node=1)
            self.c2 = self.conversion(node=2)
            self.c3 = self.conversion(node=3)
            self.c4 = self.conversion(node=4)
            self.c5 = self.conversion(node=5)
            self.scc_list = [self.c0, self.c1, self.c2, self.c3, self.c4, self.c5]
        elif self.components == 5:
            self.c0 = self.conversion(node=0)
            self.c1 = self.conversion(node=1)
            self.c2 = self.conversion(node=2)
            self.c3 = self.conversion(node=3)
            self.c4 = self.conversion(node=4)
            self.scc_list = [self.c0, self.c1, self.c2, self.c3, self.c4]
        elif self.components == 4:
            self.c0 = self.conversion(node=0)
            self.c1 = self.conversion(node=1)
            self.c2 = self.conversion(node=2)
            self.c3 = self.conversion(node=3)
            self.scc_list = [self.c0, self.c1, self.c2, self.c3]
        elif self.components == 3:
            self.c0 = self.conversion(node=0)
            self.c1 = self.conversion(node=1)
            self.c2 = self.conversion(node=2)
            self.scc_list = [self.c0, self.c1, self.c2]
        elif self.components == 2:
            self.c0 = self.conversion(node=0)
            self.c1 = self.conversion(node=1)
            self.scc_list = [self.c0, self.c1]
        elif self.components == 1:
            self.c0 = self.conversion(node=0)
            self.scc_list = [self.c0]


        self.total_k = 0


    #this method converts the contents read from the output.txt file and converts them to integers so they can be easily read
    def conversion(self, node):
        p1 = self.contents[node]
        list_item = []

        if "\n" in p1:
            for i in p1:
                try:
                    list_item.append(int(i))
                except ValueError:
                    continue
        return list_item



    def test_edge(self):

        list2 = self.edges_list.copy()
        list_index = self.scc_list.copy()

        #list that will contain the kernal graph output
        self.kg_list = []

        while len(list2) > 0:
            #print("looking at list2 {}".format(list2[0]))
            node1 = list2[0][0]
            node2 = list2[0][1]
            #for every componenent in strongly connected components
            for index, scc in enumerate(list_index, 0):
                current_index = index
                #print("looking at current component number--{}  current component--{}".format(index, scc))
                if node1 in scc:
                    current_scc = current_index

                if node2 in scc:
                    #print("current node--{} is in {} therefor\n".format(node2, index))
                    if current_scc == index:
                        list2.pop(0)
                        break
                    else:
                        #print("current component {} is connected to {}".format(current_scc, index))
                        
                        list2.pop(0)
                        self.total_k += 1
                        ##print("{} {}\n".format(current_scc, index))
                        self.kg_list.append((current_scc, index))
                        break
                else:
                    for t, n in enumerate(self.scc_list, 0):
                        if node2 in n:
                            #print("CURRENT COMPONENT--{} is connected with--{}".format(current_index, t))
                            list2.pop(0)
                            break
                            
                        break

        #int to store the total number of edges from the Kernal Graph
        self.kg_total_edges = len(self.kg_list)

    
    def kgraph(self):
        #list of all the strongley connected components
        list_index = self.scc_list.copy()
        #for every componenent in strongly connected components
        for index, scc in enumerate(list_index, 0):
            #print("looking at current component number--{}  current component--{}".format(index, scc))
            
            #for every vertex in the component
            for vertex in scc:
                #print(vertex)

                self.check_nodes(vertex=vertex, current_scc=scc, current_index=index)
                #list_index.pop(0)
                #print(list_index)

    
    def kg_print(self):
        print("the kernal graph is")
        print(kg.components)
        print(kg.total_k)

        self.final_kg = list(dict.fromkeys(kg.kg_list))

        for i in self.final_kg:
            print(i[0], i[1])

        

kg = KernalGraph(components=len(contents), contents=contents, edge_data=edges_list)

kg.test_edge()

kg.kg_print()