"""
Names: Arnika Abeysekera, Micah Hansonbrook, Sarah Ali, Tina Chen
Course: COMP123-01
Instructor: Lauren Milne
Description: This file runs tests of the csvInteraction file, the getEvents file, and the getAllStocks file (all are closely related)
"""

from stockMarket.code.csvInteraction.csvImporter import *

def runTests():
    '''Runs all CSV-related tests.'''
    test_importCSV()


def test_importCSV():
    '''Tests the importCSV file.'''
    print("Testing importCSV")
    assert importCSV('../assets/csv/test.csv')[0] == {'Year': '2020', 'Unemployment Rate': '6.7', 'Presidential Election': 'TRUE', 'Democratic Incumbent': 'FALSE', 'Democratic Congressional Count': '232', 'Republican Congressional Count': '198', 'Democratic Base': '53.6', 'Republican Base': '42.6', 'Retiring Democrats': '9', 'Retiring Republicans': '29', 'Senate Change': '4'}
    print("Testing successful.")

if __name__ == "__main__":
    runTests()