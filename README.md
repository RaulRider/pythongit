# pythongit
Sample code in python

REQUEST IP
```
import json
import requests

resp = requests.get('https://ipinfo.io/json')
print(resp.json())
print(resp.json()['ip'])
```

EXECUTE COMMANDS
Explicacion: https://pythonspot.com/python-subprocess/

Basico:
```
import subprocess
subprocess.call("command1")
subprocess.call(["command1", "arg1", "arg2"])
```
Call()
```
import subprocess
subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
# Run the command described by args. 
# Wait for command to complete, then return the returncode attribute.
```
Check_output: To get the output as a byte string
```
subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
 # Run command with arguments and return its output as a byte string.
```
Conversion de output Bytes->str y Dividir lineas del output:
```
import subprocess
s = subprocess.check_output(["ping", "-c 4", "google.com"])
output = s.decode("utf-8")
 
lines = output.split('\n') # check STRING methods https://www.w3schools.com/python/python_ref_string.asp
for line in lines:
    print(line)
```

Start a process in Python: 
This is equivalent to ‘cat test.py’. 
```
from subprocess import Popen, PIPE
process = Popen(['cat', 'test.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
Popen.wait() #If you want to wait for the program to finish you can call Popen.wait()
print stdout
```
#MAKE PYTHON CODE EXECUTABLE
```
#! /usr/bin/python3
print('Hello, world!')
```

Type chmod a+x hello.py to tell Linux that it is an executable program.
Type ./hello.py to run your program!
```
In addition, you can also use 
ln -s hello.py /usr/bin/hello
```
to make a symbolic link hello.py to /usr/bin under the name hello, then run it by simply executing hello.

Note that this mainly should be done for complete, compiled programs, if you have a script that you made and use frequently, then it might be a good idea to put it somewhere in your home directory and put a link to it in /usr/bin. 

If you want a playground, a good idea is to invoke mkdir ~/.local/bin and then put scripts in there. To make ~/.local/bin content executable the same way /usr/bin does type $PATH = $PATH:~/local/bin 
(you can add this line to your shell rc file, for example ~/.bashrc).













