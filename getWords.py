"""
Tsintzou Ioanna - 3110202
"""
def getWords(filename):
    lines = filename.readlines()
    filename.close()

    #return files words converted to lower case and splitted by space
    return [word.strip().lower() for line in lines for word in line.split()]



