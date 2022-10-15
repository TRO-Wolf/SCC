import sys



#A class to read the given input file and organize the data
#I tried to clean up and improve this from my last assignment
class ReadFile:

    def __init__(self):

        self.length = len(sys.argv)
        self.arg_string = str(sys.argv)

        with open(sys.argv[1], 'r') as f:
            contents = f.readlines()
        self.edges_list = []
        self.new_content = []

        for i in contents:
            try:
                self.new_content.append(int(i))
            except ValueError:
                self.edges_list.append(i.strip())
        self.total_vertices = self.new_content[0]
        self.total_edges = self.new_content[1]


class OldReadFile:

    def __init__(self):

        with open(sys.argv[1], 'r') as f:
            contents = f.readlines()
        self.edges_list = []
        self.node_edges_count = []

        self.vertex_string_list = []
        self.vertex_int_list = []
        for i in contents:
            try:
                self.node_edges_count.append(int(i))
            except ValueError:
                self.vertex_string_list.append(i)
        for item in self.vertex_string_list:
            if item[3:] == "\n":
                self.vertex_int_list.append((int(item[0]), int(item[2])))

class Old2ReadFile:


    def __init__(self):

        self.input_string = input("give commands here: ")

        if '.' in self.input_string:
            self.arg_location = self.input_string.find('.')

            self.file_name = self.input_string[:self.arg_location]
        
        with open(self.input_string, 'r') as f:
            contents = f.readlines()
            self.contents = contents

        self.edges_list = []
        self.node_edges_count = []

        self.vertex_string_list = []
        self.vertex_int_list = []
        
        for i in contents:
            try:
                self.node_edges_count.append(int(i))
            except ValueError:
                self.vertex_string_list.append(i)
        for item in self.vertex_string_list:
            if item[3:] == "\n":
                self.vertex_int_list.append((int(item[0]), int(item[2])))
        
        self.total_nodes = self.node_edges_count[0]
        self.total_edges = self.node_edges_count[1]


'''               
input_string = input("give commands here: ")

if '.' in input_string:
    #the index location of the . in the input string
    arg_location = input_string.find('.')

    #this is setting the filename = to the string of input_string and getting all values prior to the . in the input string
    file_name = input_string[:arg_location]
    #print(new.find('.'))
    print(file_name)
'''

class NewReadFile:


    def __init__(self):

        self.input_string = input("give commands here: ")

        if '.' in self.input_string:
            self.arg_location = self.input_string.find('.')

            self.file_name = self.input_string[:self.arg_location]
        
        with open(self.input_string, 'r') as f:
            contents = f.readlines()
            self.contents = contents

        self.edges_list = []
        self.node_edges_count = []

        self.edges_string_list = []
        self.edges_int_list = []
        
        for i in contents:
            try:
                self.node_edges_count.append(int(i))
            except ValueError:
                self.edges_string_list.append(i)
        for item in self.edges_string_list:
            if item[3:] == "\n":
                self.edges_int_list.append((int(item[0]), int(item[2])))
        
        self.edges_int_list.append((int(self.edges_string_list[-1][0]), int(self.edges_string_list[-1][2])))

        
        self.total_nodes = self.node_edges_count[0]
        self.total_edges = self.node_edges_count[1]

      


nrf = NewReadFile()

print("filename is {}".format(nrf.input_string))
print("number of nodes = {}".format(nrf.total_nodes))
print("number of edges {}".format(nrf.total_edges))
print("contents are {}".format(nrf.contents))

        




#A Class for the Nodes in a Linked List
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

#A Class for a Single Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


length = len(sys.argv)
arg_string = str(sys.argv)

with open(sys.argv[1], 'r') as f:
    contents = f.readlines()

edges_list = []
new_content = []

for i in contents:
    try:
        new_content.append(int(i))
    except ValueError:
        edges_list.append(i.strip())
total_vertices = new_content[0]
total_edges = new_content[1]

if __name__=='__main__':
    print("Number of Arguments {}".format(length))
    print("Arguments are {}".format((arg_string)))
    print(contents)
    print(total_edges)