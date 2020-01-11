import platform
import struct
import getpass

print(getpass.getuser()) # username
print("Python shell executing on", struct.calcsize("n")*8, "bit mode")

print(platform.system())
print(platform.release())
print(platform.architecture())
print(platform.machine())
print(platform.processor())
print(platform.python_build())
