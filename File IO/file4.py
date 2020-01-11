import os, string

if not os.path.exists("test"):
    os.makedirs("test")

str = "LOTR"
for s in str:
    with open(os.path.join("test", s + ".txt"), "w") as f:
        f.write(s)

# import shutil
# shutil.rmtree("test")
