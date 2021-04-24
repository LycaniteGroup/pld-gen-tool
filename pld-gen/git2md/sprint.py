import datetime
import re

from card import Card

sprintIDPattern = re.compile('#(\d+)')
sprintDatePattern = re.compile('\((\d+)/(\d+)/(\d+)\)')

class Sprint:

    def __init__(self, project):
        self.cards = []
        self.project = project
        self.number = int(sprintIDPattern.findall(project.name)[0])

        self.dateMatch = sprintDatePattern.findall(project.name)[0]
        self.day = int(self.dateMatch[0])
        self.month = int(self.dateMatch[1])
        self.year = int(self.dateMatch[2])

        self.date = datetime.datetime(day=self.day, month=self.month, year=self.year)

        for column in project.get_columns():
            for card in column.get_cards():
                content = card.get_content()
                self.cards.append(Card(content))
    
    def getName(self):
        return self.project.name

    def isOpen(self):
        return self.project.state == 'open'
    
    def isClose(self):
        return self.project.state == 'close'
    
    def getSprintNumber(self):
        return self.number
    
    def getDay(self):
        return self.day
    
    def getMonth(self):
        return self.month
    
    def getYear(self):
        return self.year
    
    def getDate(self):
        return date
    
    def getCards(self):
        return self.cards