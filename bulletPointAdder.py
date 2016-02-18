#!/usr/bin/python3.4

# bulletPointAdder.py - Adds bullet points to the start of each line of text in the clipboard.

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
     lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
print(text)

pyperclip.copy(text)