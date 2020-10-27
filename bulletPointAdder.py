#! python3
# bulletPointAdder.py - Adds wiki bulletpoints to start of each line in clipboard

import pyperclip
text = pyperclip.paste()

#TODO: Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): #loop though all indexes in the "lines" list
    lines[i] = '*' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)
