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


'''
# Third command
proc3 = subprocess.Popen(['python3', 'textbot.py'])
proc3.wait()
print('Process 3 is Completed!!!')

# Fourth command
proc4 = subprocess.Popen(['python3', 'photocomplete.py'])
proc4.wait()

# Fifth command
proc5 = subprocess.Popen(['python3', 'fbpost.py'])
proc5.wait()

# Six command
proc6 = subprocess.Popen(['python3', 'fbphoto.py'])
proc6.wait()

print('\n Run Command Success')

'''