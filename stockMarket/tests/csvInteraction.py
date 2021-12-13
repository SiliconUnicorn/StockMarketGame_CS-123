"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file runs tests of the csvInteraction file
"""

from stockMarket.code.csvInteraction.csvImporter import *

def runTests():
    '''Runs all CSV-related tests.'''
    test_importCSV()
    test_makeList()
    test_generateDictionary()

def test_importCSV():
    '''Tests the importCSV function.'''
    print("Testing importCSV")
    assert importCSV('../assets/csv/test.csv')[0] == {'Year': '2020', 'Unemployment Rate': '6.7', 'Presidential Election': 'TRUE', 'Democratic Incumbent': 'FALSE', 'Democratic Congressional Count': '232', 'Republican Congressional Count': '198', 'Democratic Base': '53.6', 'Republican Base': '42.6', 'Retiring Democrats': '9', 'Retiring Republicans': '29', 'Senate Change': '4'}
    print("Testing successful.")

def test_makeList():
    '''Tests the makeList function'''
    print("Testing makeList()")
    orgFile = open('../assets/csv/test.csv', 'r')
    header = orgFile.readline().strip('\n')
    assert makeList(header) == ['Year', 'Unemployment Rate', 'Presidential Election', 'Democratic Incumbent', 'Democratic Congressional Count', 'Republican Congressional Count', 'Democratic Base', 'Republican Base', 'Retiring Democrats', 'Retiring Republicans', 'Senate Change']
    orgFile.close()
    print("Testing Successful")

def test_generateDictionary():
    '''Tests the generateDictionary() function.'''
    print("Testing generateDictionary()")
    orgFile = open('../assets/csv/test.csv', 'r')
    header = orgFile.readline().strip('\n')
    header = makeList(header)
    line = orgFile.readline()
    newLine = makeList(line.strip('\n'))
    assert generateDictionary(header, newLine) == {'Year': '2020', 'Unemployment Rate': '6.7', 'Presidential Election': 'TRUE', 'Democratic Incumbent': 'FALSE', 'Democratic Congressional Count': '232', 'Republican Congressional Count': '198', 'Democratic Base': '53.6', 'Republican Base': '42.6', 'Retiring Democrats': '9', 'Retiring Republicans': '29', 'Senate Change': '4'}
    orgFile.close()
    print('Testing Successful')

if __name__ == "__main__":
    runTests()