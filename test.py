import sys

from sympy import Ne, content

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

        


nrf = NewReadFile()

print("filename is {}".format(nrf.input_string))
print("number of nodes = {}".format(nrf.total_nodes))
print("number of edges {}".format(nrf.total_edges))
print("contents are {}".format(nrf.contents))


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



#print(new[1])


'''
while True:
    data = input("Please Enter Filename Here: ")
    if "Exit" == data:
        break
    print("Processing Message from input {}".format(data))

    with open(sys.argv[1], 'r') as f:
        contents = f.read()
    print(contents)


print("Done")
'''