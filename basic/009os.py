import os

# os.system('cls')
os.system("dir")
print(os.name)
print(os.environ)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))
print(os.path.isdir(__file__))
print(os.path.isabs(__file__))
print(os.path.isfile(__file__))
print(os.path.getsize(__file__), "bytes")
print(os.path.expanduser("~"))
print(
    [
        f
        for f in os.listdir("\\Users\\dell\\Desktop")
        if os.path.isdir(os.path.join("\\Users\\dell\\Desktop\\" + f))
    ]
)

