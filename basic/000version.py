# 1
import sys
print (sys.version)
print (sys.api_version)
print (sys.version_info)


# 2
import subprocess
#b'Python 3.7.3\r\n'  -  without decode()
pythonVersion = subprocess.check_output(["git", "--version"])
print (pythonVersion.decode())