#!/usr/bin/env python3

"""Run script with:

    cd template
    python3 script.py accounts.php actions.php admin.php ...
"""

from sys import argv
from googletrans import Translator

for filename in argv[1:]:
    lines = None
    with open(filename) as f:
        lines = f.readlines()

    translator = Translator()

    with open('../sv/{}'.format(filename), 'w') as f:
        f.write(lines[0])
        for line in lines[1:-1]:
            to_translate = line[3:-9]
            start = line[:-3]
            end = line[-3:-1]
            translated_phrase = translator.translate(to_translate, src='en', dest='sv').text
            f.write(start + translated_phrase + end + "\n")
        f.write(lines[-1])

