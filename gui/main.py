from algo2 import *
from algo1 import *
"""
trainstream = TCPstream(100,40)
trainstream = trainPhase(100,40,10,'darpatrain')
f = open('thresholdP','w')
f.write(str(trainstream.thresholdProbability))
f.close()
"""
teststream = TCPstream(100,40)
#teststream.probabilityArray = trainstream.probabilityArray
teststream = deploy(teststream,10,'kddAttack')
