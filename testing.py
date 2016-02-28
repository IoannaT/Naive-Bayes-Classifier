"""
Tsintzou Ioanna - 3110202
"""
import os
from getWords import getWords

def testing (hamtesting, spamtesting, hamTrainingSet, spamTrainingSet, prHam, prSpam):

    hamham = []     #true positive
    hamspam = []    #true negative
    spamspam = []   #false positive
    spamham =[]     #false negative
    hamMails = 0
    spamMails = 0

    #open ham testing mails
    for filename in os.listdir(hamtesting):
        hamMails += 1
        curFile = open(hamtesting + filename, 'r')
        #get all words
        hamtestwords = getWords(curFile)
        #find the type of mail
        email_category = category (hamtestwords, hamTrainingSet,spamTrainingSet, prHam, prSpam)
        #put it into the right list
        if email_category == 'ham':
            hamham.append(filename)
        elif email_category == 'spam':
            hamspam.append(filename)

    #open testing mails and get all of their words
    for filename in os.listdir(spamtesting):
        spamMails += 1
        curFile = open(spamtesting + filename, 'r')
        #get all words
        spam_test_words = getWords(curFile)
        #find the type of mail
        email_category = category (spam_test_words, hamTrainingSet,spamTrainingSet, prHam, prSpam)
        #put it into the right list
        if email_category == 'spam':
            spamspam.append(filename)
        elif email_category == 'ham':
            spamham.append(filename)

    totalMails = hamMails + spamMails
    return hamham, hamspam, spamspam, spamham, totalMails



#defines if a mail is either ham or spam
def category(words, hamTrainingSet, spamTrainingSet, prHam, prSpam):

    prHamVector = 0
    prSpamVector = 0

    #P(Ham | email) = < P(Ham | word1) * P(Ham|word2) * .... P(Ham | wordN) > * P(Ham)
    for word in words:
        if word in hamTrainingSet :
            prHamVector *= hamTrainingSet[word]

    prHamEmail = prHam * prHamVector

    #P(Spam | email) = < P(Spam | word1) * P(Spam | word2) * .... P(Spam | wordN) > * P(Spam)
    for word in spamTrainingSet:
        if word in spamTrainingSet :
            prSpamVector *= spamTrainingSet[word]

    prSpamEmail = prSpam * prSpamVector


    return 'ham' if prHamEmail > prSpamEmail else 'spam'
