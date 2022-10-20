edges_list = [(0, 1),
 (1, 2),
 (2, 3),
 (3, 1),
 (3, 5),
 (3, 4),
 (4, 6),
 (5, 6),
 (5, 7),
 (6, 8),
 (7, 4),
 (7, 9),
 (8, 7)]

#this reads from the output.txt file
with open('output.txt', 'r') as f:
    contents = f.readlines()

class KernalGraph:


    def __init__(self, components, contents, edge_data):
        
        self.contents = contents

        #number of strongly connected components
        self.components = components

        self.edges_list = edge_data
        self.node_list = []
        for i in self.edges_list:
            self.node_list.append(i[0])

        #the total number of connected components
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


    '''
    def check_nodes1(self, nodes, input_list):
        list1 = input_list
        node = list1[0]
        current_component = node
        #while list1 > 0:
        for x in list1:
            for i in self.edges_list:
                if node in i[0]:
                    edge_end = i[1]
                if edge_end in list1:
                    continue
                elif edge_end not in list1:
                    for n in self.scc_list:
                        if edge_end in n:
                            print(current_component, n)
                            return (current_component, n)'''
    
    


    def test_edge(self):



        list2 = self.edges_list.copy()

        list_index = self.scc_list.copy()


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
                        print("{} {}\n".format(current_scc, index))
                        break
                else:
                    for t, n in enumerate(self.scc_list, 0):
                        if node2 in n:
                            #print("CURRENT COMPONENT--{} is connected with--{}".format(current_index, t))
                            list2.pop(0)
                            break
                            
                        break



    
    #this is a method designed to check all of the nodes to 
    def check_nodes(self, vertex, current_scc, current_index):
        list1 = current_scc
        #print(list1)
        node = vertex
        #print("current node is {}".format(node))
        
        current_component = node
        copied = self.edges_list.copy()
        print()
        
        #print(node)
        edge_end = None
        for i in copied:
            #if node in i:
            if node == i[0]:
                #print("current node is {} in component {}".format(node, i[0]))
                edge_end = i[1]
                #print("current edge end is {}".format(edge_end))
            
                #if the end of this edge is in this current component continue
                if edge_end in list1:
                    continue

                #if the end of this edge is not in the current component, find out where it is
                elif edge_end not in list1:
                    #print("current end edge {} is not in {}".format(edge_end, list1))
                    for t, n in enumerate(self.scc_list, 0):
                        #print("component {}".format(n))
                        if edge_end in n:
                            #print("current end edge {} is in {}".format(edge_end, t))
                            self.total_k += 1
                            print("current component--{} is connected with--{}".format(current_index, t))
                            print(" ")
                            return (current_component, n)
                


            #for i, n in enumerate(kg.scc_list, 0):
            #    print(i, n)


    
    
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

kg = KernalGraph(components=len(contents), contents=contents, edge_data=edges_list)

kg.test_edge()



        

        