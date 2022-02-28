#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# FMitsiopoulos, 2022-Feb-27, replace data structure with dictionaries, 
#   add fucntionality of loading existing data and deleting entries
#------------------------------------------#

# Delcare variable

strChoice = '' # User input
dicRow = {}  # Dictionary variable
lstDic = []
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    
    if strChoice == 'x':
        break
        # 5. Exit the program if the user chooses so

# Loading existing data
    if strChoice == 'l':
        objFile = open(strFileName, 'r') 
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': (lstRow[0]), 'Title': lstRow[1], 'Artist': lstRow[2]}
            lstDic.append(dicRow)
        objFile.close()

# Get user input as a dictionary
    elif strChoice == 'a': 
        # 2. Add data to the table (2d-list) each time the user wants to add data
        intID = int(input('Enter an ID: '))
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstDic.append(dicRow)

# Display data to user
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstDic:
            print(*row.values(), sep = ', ')

# Allow user to delete entry
    elif strChoice == 'd':
        value = ''
        row = {}
        deleteDic = int(input('Enter the CD entry you wish to delete using it\'s corresponding ID: '))
        #iterate through list of dicts
        for row in lstDic:         
        #iterate through values in dicts
            for key, value in row.items():
                # Identify keyword
                if value == deleteDic:
                    #Delete Dictionary
                    row.clear()
                    break

# Save text to file
    elif strChoice == 's':
            # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        strRow = ''
        for row in lstDic:
            for items in row.items():
                strRow += str(items) + ','
            strRow = strRow[:-1] + '\n'
        objFile.write(strRow)
        objFile.close()
    
else:
        print('Please choose either l, a, i, d, s or x!')
