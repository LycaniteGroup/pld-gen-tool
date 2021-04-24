import sys
import os
import re
import datetime
from pathlib import Path
import json

sprintNumberPattern = re.compile('Sprint #(\d+)')

fileNames = [
    ('index.md', '### Sprint Planification'),
    ('bilan.md', '### Bilan')
]

sprintPath = '/var/sprints'

folders = []
for dir in os.listdir('%s' % sprintPath):
    number = int(sprintNumberPattern.findall(dir)[0])
    folders.append((number, dir))

folders.sort(key=lambda x: x[0])

version = {}

with open('/var/version.json', 'r') as versionFile:
    version = json.loads(versionFile.read())

with open('/var/md2html/docs/index.md', 'w') as file:
    now = datetime.date.today()
    file.write('<!-- ---\n')
    file.write('hide:\n')
    file.write('  - navigation # Hide navigation\n')
    file.write('  - toc        # Hide table of contents\n')
    file.write('--- -->\n')
    file.write('\n')
    file.write('![Placeholder](./assets/lycanite.png){: .center align=center style="height:514px;width:389px" }\n')
    file.write('<br>\n')
    file.write('# **P**roject **L**og **D**ocument <br>**Revision %s (%s)**\n' % (version.get('revision'), now.strftime('%d-%m-%Y')))

    for folder in folders:
        found = False
        for fileName in fileNames:
            path = '%s/%s/%s' % (sprintPath, folder[1], fileName[0])
            if os.path.exists(path):
                found = True

        if found:
            file.write('\n')
            file.write('## %s\n' % folder[1])
            file.write('\n')
            for fileName in fileNames:
                path = '%s/%s/%s' % (sprintPath, folder[1], fileName[0])
                if os.path.exists(path):
                    file.write(fileName[1]+'\n')
                    file.write('\n')
                    with open(path, 'r') as mdFile:
                        file.write(mdFile.read()+'\n')
        