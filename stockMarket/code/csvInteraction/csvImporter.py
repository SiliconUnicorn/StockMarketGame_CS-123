'''
File: csv_main.py
Project: Stock Market Game
Date: 5 Nov 2021
Author(s): Micah Hansonbrook
'''

def importCSV(path):
    '''
    Imports a CSV from a given filepath
    :param path: The path
    :return: A very orderly list of dictionaries
    '''
    orgFile = open(path, 'r')
    header = orgFile.readline().strip('\n')
    header = makeList(header)
    data = []
    for line in orgFile:
        newLine = makeList(line.strip('\n'))
        data.append(generateDictionary(header, newLine))

    orgFile.close()
    return (data)

def makeList(csvLine):
    '''
    Makes a CSV string into a list
    :param csvLine: The string
    :return: A list
    '''
    resultList = []
    currentItem = ''
    for char in csvLine:
        if char != ',':
            currentItem += char
        else:
            resultList.append(currentItem)
            currentItem = ''
    return resultList


def generateDictionary(header, line):
    '''
    Generates a dictionary from the CSV header and an individual line
    :param header: The header of the CSV
    :param line: The line being read
    :return: A dictionary
    '''
    dictionary = {}
    for i in range(len(header)):
        dictionary[header[i]] = line[i]
    return dictionary


if __name__ == "__main__":
    print(importCSV('../../assets/csv/test.csv'))
