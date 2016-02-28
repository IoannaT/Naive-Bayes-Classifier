"""
Tsintzou Ioanna - 3110202

smoothing using Laplace method
for each word in Training Set
1.Increase by 1 the Xmails number
2.Increase by 2 the totalMails number
"""
def Laplace(hamSet, spamSet, hamMails, spamMails, totalMails) :

    for hamWord in hamSet :
        hamSet[hamWord] += 1
        hamSet[hamWord] /= float(totalMails+2)

    for spamWord in spamSet :
        spamSet[spamWord] += 1
        spamSet[spamWord] /= float(totalMails+2)

    return hamSet, spamSet