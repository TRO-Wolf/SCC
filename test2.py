import sys

#data = input("Please Enter Filename Here: ")
length = len(sys.argv)
arg_string = str(sys.argv)

with open(sys.argv[1], 'r') as f:
        contents = f.read()


print("Number of Arguments {}".format(length))
print("Arguments are {}".format((arg_string)))

print(contents)