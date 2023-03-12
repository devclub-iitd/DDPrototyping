import os

path = "/var/lib/mfs/test.txt"

# if not os.path.exists(os.path.dirname(path)):
#     os.makedirs(os.path.dirname(path))

if os.path.exists(path):
    with open(path, "r") as f:
        print(f.read())
    os.remove(path)
else:
    print("File not found!")


if __name__ == "__main__":
    print("File read successfully from webB!")
