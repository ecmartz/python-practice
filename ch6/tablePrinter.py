#!/usr/bin/python3.4

tableData = [['apples','oranges','cherries','bananas'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

# Per the hint
colWidth = [0] * len(tableData)

# Who knew you had to transpose this list of lists
def matrixTranspose( matrix ):
    if not matrix: return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]

def printTable(argData):
    # Copy of transpose
    argDataTrans = matrixTranspose(argData)
    # Get longest string in each
    for sub in range(len(argData)):
        for i in argData[sub]:
            if(len(i)>colWidth[sub]):
                colWidth[sub] = len(i)
    
    # Get max column width
    maxCol = max(colWidth)
    
    # Now print it using the transposed array
    for j in range(len(argDataTrans)):
        for k in range(len(argDataTrans[j])):
            print(argDataTrans[j][k].rjust(maxCol),end='')
        print()

if __name__ == '__main__':
    printTable(tableData)