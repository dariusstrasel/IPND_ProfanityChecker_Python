# Title: Profanity Filter
# Author Darius 'Alkarion' Strasel
# Todo: pass output in a more meaningful way

import urllib.request

def read_text():
    """This function opens a specified file, saves its contents to memory, and begins processing according to batch
    size."""
    document = open('C:/users/siruk/desktop/movie_quotes.txt', "r")
    contents_of_file = document.read()
    document.close()
    process_line(contents_of_file, 2)


def openConnection(string):
    """This function opens a connection to the profanity server using the input as the value to query."""
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + string)
    output = connection.read()
    print(output)
    connection.close


def process_line(line, batchSize):
    """This function will parse an input string and send values to the profanity checked based on the batched size."""
    newLine = line.split()
    pointer = 0
    indexEnd = 0
    indexStart = 0
    for i in range(0, len(newLine)):
        indexEnd = indexEnd + 1
        pointer = pointer + 1
        if pointer == batchSize:
            #print(newLine[indexStart:indexEnd])
            openConnection("%20".join(newLine[indexStart:indexEnd]))
            indexStart = indexStart + pointer
            pointer = 0
    if indexEnd - indexStart < batchSize:
        openConnection("%20".join(newLine[indexStart:len(newLine)]))


read_text()