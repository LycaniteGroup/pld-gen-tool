
import helper

predicates = [
    ('Website', lambda card: card.isFromWebsite()),
    ('Driver', lambda card: card.isFromDriver()),
    ('Application', lambda card: card.isFromApplication()),
    ('Tools', lambda card: card.isFromTool()),
]

def diagram2Markdown(sprint, callback):
    labels = set()
    for card in sprint.cards:
        labels = labels.union(card.getLabelNames())

    def labelState(label):
        if type(label) is list:
            for l in label:
                if l in labels:
                    return ':::inprogress'
            return ''
        return label in labels and ':::inprogress' or ''

    # Legend diagram
    callback('!!! note "Diagram"')
    callback()
    callback('\t```mermaid')
    callback('\tflowchart TD')
    callback('\t\tclassDef inprogress fill:#0c7dba;')
    callback('\t\tsubgraph Legende')
    callback('\t\t\tInProgress[En cours ce sprint]:::inprogress ')
    callback('\t\tend')
    callback('\t```')
    # Project Diagram
    callback('\t```mermaid')
    callback('\tflowchart TD')
    callback('\t\tclassDef inprogress fill:#0c7dba;')
    callback()
    callback('\t\tLycanite[Lycanite]:::inprogress --> Website[Website]%s' % labelState('website'))
    callback('\t\tLycanite --> Solution[Solution]%s' % labelState(['solution', 'vfs', 'kernel mode driver', 'service', 'app']))
    callback('\t\tWebsite --> Front[Frontend]%s' % labelState('frontend'))
    callback('\t\tWebsite --> Back[Backend]%s' % labelState('backend'))
    callback('\t\tSolution --> Application[Application]%s' % labelState('app'))
    callback('\t\tSolution --> VFS[Virtual File System]%s' % labelState('vfs'))
    callback('\t\tSolution --> Service[Service]%s' % labelState('service'))
    callback('\t\tSolution --> KernelDriver[Kernel Driver]%s' % labelState('kernel mode driver'))
    callback('\t```')
    callback()

def featureProgress2Markdown(sprint, callback):
    callback('!!! tip "Features Progression Status"')

    batchs = []
    for predicate in predicates:
        batch = []
        for card in sprint.cards:
            if predicate[1](card):
                batch.append(card)
        batchs.append(batch)
    
    first = True
    for i in range(len(batchs)):
        if len(batchs[i]) > 0:
            if not first:
                callback()
                callback('\t<br>')
                callback()
            
            callback('\t**%s**' % predicates[i][0])
            callback()

            table = [
                ['Feature'] + ['[%s](#%s)' % (card.getTitle(), helper.anchor([sprint.getName(), predicates[i][0], card.getTitle()])) for card in batchs[i]],
                ['Progress'] + ['[=%d%% "%d / %d (%d%%)"]' % (card.getProgressPercentage(), card.countFinishedDefinition(), len(card.getDefinitionOfDone()), card.getProgressPercentage()) for card in batchs[i]]
            ]

            callback(helper.generateTable(table, linePrefix='\t'))
            callback()
            
            totalDefinitions = sum([len(card.getDefinitionOfDone()) for card in batchs[i]])
            totalDone = sum([card.countFinishedDefinition() for card in batchs[i]])
            totalPercent = totalDone / totalDefinitions * 100
            overallTable = [
                ['Overall Progress'],
                ['[=%d%% "%d / %d (%d%%)"]' % (totalPercent, totalDone, totalDefinitions, totalPercent)]
            ]

            callback(helper.generateTable(overallTable, linePrefix='\t', left=True))

            first = False


def card2Markdown(card, callback):
    callback('!!! info "[%s](%s)"' % (card.getTitle(), card.getUrl()))
    storyTable = [
        ['As', card.getAs()],
        ['I want', card.getIWant()]
    ]
    callback(helper.generateTable(storyTable, linePrefix='\t', left=True))
    callback()
    descTable = [
        ['Description', card.getDescription().replace('\n','<br>')]
    ]
    callback(helper.generateTable(descTable, linePrefix='\t', left=True))
    callback()
    worktimeTable = [
        ['Working Day(s)', card.getWorkingDays()],
        ['Working People(s)', card.getWorkerCount()]
    ]
    callback(helper.generateTable(worktimeTable, linePrefix='\t', center=True))
    callback()
    callback('\t**Definition of Done**')
    callback()
    for check in card.getDefinitionOfDone():
        callback('\t- [%s] %s' % (check[0] and 'x' or ' ', check[1]))
    callback()
    callback('\t[=%d%% "%d / %d (%d%%)"]' % (card.getProgressPercentage(), card.countFinishedDefinition(), len(card.getDefinitionOfDone()), card.getProgressPercentage()))

def sprintCards2Markdown(sprint, callback):
    batchs = []
    for predicate in predicates:
        batch = []
        for card in sprint.cards:
            if predicate[1](card):
                batch.append(card)
        batchs.append(batch)
    
    for i in range(len(batchs)):
        if len(batchs[i]) > 0:
            callback('#### %s' % predicates[i][0])
            for card in batchs[i]:
                callback()
                callback('<a id="%s"></a>' % helper.anchor([sprint.getName(), predicates[i][0], card.getTitle()]))
                card2Markdown(card, callback)
            callback()
            callback('<br>')
            callback()

def sprint2Markdown(sprint, callback):
    ## Diagram
    diagram2Markdown(sprint, callback)
    # Progression status
    featureProgress2Markdown(sprint, callback)
    callback()
    callback('<br>')
    callback()
    # Cards informations per repo
    sprintCards2Markdown(sprint, callback)
    