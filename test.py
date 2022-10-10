import sys

class NewReadFile:

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


nrf = NewReadFile()
print(nrf.vertex_int_list)


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