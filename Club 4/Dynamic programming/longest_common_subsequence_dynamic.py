#src: https://www.techiedelight.com/longest-common-subsequence/
def print_table(table):
    for row in table:
        print(row)

def LCS_Dynamic(x, y):
    #print(x, y)

    lenX = len(x)
    lenY = len(y)
    table = [[0 for columns in range(lenX + 1)] for rows in range(lenY + 1)]
    
    #Base cases, when either string length is 0
    for i in range(lenX + 1):
        #columns
        table[0][i] = 0
    for i in range(1, lenY + 1):
        #rows
        table[i][0] = 0
    
    #print_table(table)

    for i in range(1, lenY + 1):
        for j in range(1, lenX + 1):
            #If the last character of x and y matches
            if x[j-1] == y[i-1]:
                table[i][j] = table[i-1][j-1] + 1
            #Else if the characters dont match
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    #print_table(table)
    return table[lenY][lenX]

x = input()
y = input()

print(LCS_Dynamic(x, y))