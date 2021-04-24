import re
import helper

separatorPattern = re.compile('[-]{3}[-]*')
checklistPattern = re.compile('[\t ]*\- \[(.)\] (.+)')
commentPattern  = re.compile('<![-]+[^-]+[-]+>')

class Card:
    def __init__(self, card):
        self.card = card
        self.labels = card.labels
        self.title = card.title
        self.url = card.html_url
        self.labelnames = set()
        for label in self.labels:
            self.labelnames.add(label.name)
        
        self.fromWebsite = 'website' in self.labelnames
        self.fromSoftware = 'software' in self.labelnames
        self.fromDriver = 'kernel mode driver' in self.labelnames
        self.fromApplication = 'app' in self.labelnames
        self.fromTool = 'tool' in self.labelnames
        self.body = commentPattern.sub('', card.body.replace('\r', ''))

        self.desc = ''
        self.asUser = ''
        self.IWant = ''
        self.workdays = 0
        self.people = 0
        self.defdone = []
        self.progress = 0

        check = ''
        linejump = True
        for line in self.body.split('\n'):
            if len(line) == 0: # Skip empty line
                if check != 'desc' or len(self.desc) == 0:
                    continue
            elif line.lower() == '## user story':
                check = 'userstory'
                continue
            elif line.lower() == '## description':
                check = 'desc'
                continue
            elif line.lower() == '## definition of done':
                check = 'defdone'
                continue
            elif separatorPattern.match(line): # Skip separator
                check = 'defdone'
                continue
            
            if check == 'userstory':
                if line.lower().startswith('as:'):
                    self.asUser = line[3:].lstrip()
                elif line.lower().startswith('i want:'):
                    self.IWant = line[7:].lstrip()
            elif check == 'desc':
                if not linejump or len(line) > 0:
                    self.desc += line + '\n'
                linejump = len(line) == 0
            elif check == 'defdone':
                if line.lower().startswith('working days:'):
                    self.workdays = helper.parseInt(line[13:].lstrip())
                elif line.lower().startswith('working people:'):
                    self.people = helper.parseInt(line[15:].lstrip())
                elif match := checklistPattern.findall(line):
                    if len(match) > 0:
                        self.defdone.append((match[0][0] != ' ', match[0][1]))
        
        if len(self.defdone) > 0:
            for checkbox in self.defdone:
                if checkbox[0]:
                    self.progress += 1
            self.progress /= len(self.defdone)
        
        self.desc = self.desc.strip()

    def isOpen(self):
        return self.card.state == 'open'

    def isClose(self):
        return self.card.state == 'close'

    def getTitle(self):
        return self.title
    
    def getUrl(self):
        return self.url

    def getLabels(self):
        return self.card.labels

    def getLabelNames(self):
        return self.labelnames
    
    def isFromWebsite(self):
        return self.fromWebsite
    
    def isFromSoftware(self):
        return self.fromSoftware

    def isFromApplication(self):
        return self.fromApplication

    def isFromDriver(self):
        return self.fromDriver
    
    def isFromTool(self):
        return self.fromTool

    def getAs(self):
        return self.asUser

    def getIWant(self):
        return self.IWant
    
    def getDescription(self):
        return self.desc

    def getWorkerCount(self):
        return self.people
    
    def getWorkingDays(self):
        return self.workdays

    def getDefinitionOfDone(self):
        return self.defdone

    def getProgressPercentage(self):
        return self.progress * 100