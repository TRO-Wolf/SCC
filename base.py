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