"""
Tsintzou Ioanna - 3110202
"""
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import precision_recall_curve

from constructTrainingSet import constructTrainingSet
from Laplace import Laplace
from testing import testing

# ================= TRAINING =====================
hamtraining = os.getcwd() + '/bare/hamtraining/'
spamtraining = os.getcwd() + '/bare/spamtraining/'

#to training set ginetai testing set
#hamtraining = os.getcwd() + '/bare/hamtesting/'
#spamtraining = os.getcwd() + '/bare/spamtesting'

#fakelos lemm-stop gia eksetash
#hamtraining = os.getcwd() + '/lemm-stop/hamtraining/'
#spamtraining = os.getcwd() + '/lemm-stop/spamtraining/'

#construct the training sets for ham and spam mails
hamTrainingSet, spamTrainingSet, hamMails, spamMails = constructTrainingSet(hamtraining, spamtraining)

# ================ PROBABILITIES =================
#calculate the probabilties
totalMails = hamMails + spamMails
prHam = hamMails / float(totalMails)
prSpam = spamMails / float (totalMails)

# ================ SMOOTHING =====================
#Apply Laplace method
hamTrSmooth, spamTrSmooth = Laplace(hamTrainingSet, spamTrainingSet, hamMails, spamMails, totalMails)

# ================ TESTING =======================
hamtesting = os.getcwd() + '/bare/hamtesting/'
spamtesting = os.getcwd() + '/bare/spamtesting/'

#hamtesting = os.getcwd() + '/bare/hamtraining/'
#spamtesting = os.getcwd() + '/bare/spamtraining/'

#hamtesting = os.getcwd() + '/lemm-stop/hamtesting/'
#spamtesting = os.getcwd() + '/lemm-stop/spamtesting/'

#Read the every mail in testing sets and predict if it's ham | spam
hamham, hamspam, spamspam, spamham, totalTestedMails = testing(hamtesting, spamtesting, hamTrSmooth, spamTrSmooth, prHam, prSpam)


# ================ Calculate accuracy, precision and recall ===============
tp = len(hamham)
tn = len(hamspam)
fp = len(spamspam)
fn = len(spamham)

print 'True positive Emails: ', tp
print 'True negative Emails: ', tn
print 'False positive Emails: ', fp
print 'False negative Emails: ', fn
print 'Total Tested Emails: ', totalTestedMails

if totalTestedMails != 0:
    print
    print 'Accuracy: ', (tp+tn)/float(totalTestedMails)
else :
    print 'Accuracy can not be calculated'
if (tp+fp) != 0:
    print 'Precision: ', tp/float(tp+fp)
else :
    print 'Precision can not be calculated'
if (tp+fn) != 0:
    print 'Recall: ', tp/float(tp+fn)
else:
    print 'Reacall can not be calculated'

