import os
import subprocess

# First command
proc1 = subprocess.Popen(['node', 'index.js', '--ticker', 'USDT', '--fiat', 'MMK', '--operation', 'BUY'])
proc1.wait()
print('Process 1 is Completed!!')

# Second command
proc2 = subprocess.Popen(['node', 'index.js', '--ticker', 'USDT', '--fiat', 'THB', '--operation', 'SELL'])
proc2.wait()
print('Process 2 is Completed!!!')

# Third command
proc3 = subprocess.Popen(['python3', 'textgenerator.py'])
proc3.wait()
print('Process 3 is Completed!!!')

# Fourth command
proc4 = subprocess.Popen(['python3', 'fbpost.py'])
proc4.wait()