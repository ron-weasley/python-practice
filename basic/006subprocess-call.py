import subprocess
from subprocess import call, check_output

call(["attrib", "*.py"])
call("type test1.txt", shell=True)