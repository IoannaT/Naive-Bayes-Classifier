"""
Tsintzou Ioanna - 3110202
"""
import os
from getWords import getWords
def constructTrainingSet(hamtraining, spamtraining):

    #number of spam and hum Mails
    spamMails = 0
    hamMails = 0

    hamTrainingSet = {}
    spamTrainingSet = {}

    #Create Ham's Training Set
    for filename in os.listdir(hamtraining):
            curFile = open(hamtraining + filename, 'r')

            #create a list of words
            hamWords = getWords(curFile)
            hamMails += 1

            for word in hamWords :
                #if word exists in training Set increase its frequency.
                if word in hamTrainingSet :
                    hamTrainingSet[word] += 1
                #else create a new entry for thw new word
                else :
                    hamTrainingSet[word] = 1

    #create Spam's Training Set
    for filename in os.listdir(spamtraining):
        curFile = open(spamtraining + filename, 'r')

        #create a list of words
        spamWords = getWords(curFile)
        spamMails += 1

        for word in spamWords :
            #if word exists in training Set increase its value.
            if word in spamTrainingSet :
                spamTrainingSet[word] += 1
            #else create a new entry for this word
            else :
               spamTrainingSet[word] = 1

    print 'Number of Ham Training Emails: ', hamMails
    print 'Number of Spam Training Emails: ', spamMails

    return hamTrainingSet, spamTrainingSet, hamMails, spamMails