import re
_nonAlphaPattern = re.compile("[^0-9a-zA-Z]+")

def generateTable(table, linePrefix='', left=False, right=False, center=False):
    mdtable = ''

    sizes = []
    longestColumn = 0
    for i in range(len(table)):
        sizes.append(0)
        column = table[i]
        longestColumn = max(longestColumn, len(column))
        for j in range(len(column)):
            sizes[i] = max(sizes[i], len(str(column[j])))
    
    # table header
    mdtable += linePrefix
    for i in range(len(table)):
        mdtable += '| %s '  % str(table[i][0]).ljust(sizes[i])
    mdtable += '|\n'
    # table separator
    mdtable += linePrefix
    for i in range(len(table)):
        centerPrefix = '-' * sizes[i]
        if left or center:
            centerPrefix = ':'+centerPrefix[1:] 
        if right or center:
            centerPrefix = centerPrefix[:-1] + ':' 
        mdtable += '| %s '  % (centerPrefix)
    mdtable += '|\n'
    # table columns
    for i in range(1,longestColumn): # skip header
        mdtable += linePrefix
        for j in range(len(table)):
            if len(table[j]) > i:
                mdtable += '| %s ' % str(table[j][i]).ljust(sizes[j])
            else:
                mdtable += '| %s ' % (' ' * sizes[j])
        mdtable += '|\n'

    return mdtable[:-1]

def parseInt(value, default=0):
    try:
        return int(value)
    except:
        return default

def anchor(elements):
    return '-'.join(
        list(
            map(
                lambda x: 
                    _nonAlphaPattern.sub('-', str(x))
                    .strip('-'),
                elements
            )
        )
    )
    
