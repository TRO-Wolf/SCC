import sys

while True:
    data = input("Please Enter Filename Here: ")
    if "Exit" == data:
        break
    print("Processing Message from input {}".format(data))

    with open(sys.argv[1], 'r') as f:
        contents = f.read()
    print(contents)


print("Done")