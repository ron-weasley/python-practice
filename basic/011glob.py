import glob
import os

files = glob.glob("*.*")
# getctime-creation time  getmtime-modification time  getatime-access time
# (for the present folder we are in)
files.sort(key=os.path.getctime)
print("\n".join(files))