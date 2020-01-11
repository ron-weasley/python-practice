with open("test.txt", "w") as f:
    f.write("Tweety Bird\n")
    f.write("tawt ")
    f.write("ti taw a\n")
    f.writelines("Romulan")
    f.close()

# Append
f = open("test.txt", "a")
f.write("\n000")

# file size
import os
print (os.stat('test.txt').st_size)
