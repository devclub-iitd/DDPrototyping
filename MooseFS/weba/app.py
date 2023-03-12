import os

path = "/var/lib/mfs/test.txt"

if not os.path.exists(os.path.dirname(path)):
    os.makedirs(os.path.dirname(path))

with open(path, "w") as f:
    f.write("Hello World! from webA")


if __name__ == "__main__":
    print("File written successfully from webA!")
