from algo2 import *
from algo1 import *

t = 0.111
trainstream = TCPstream(100,40,t)
trainstream = trainPhase(100,40,10,"kddTrain",t)
f = open('thresholdP','w')
f.write(str(trainstream.thresholdProbability))
f.close()
teststream = TCPstream(100,40,t)
teststream.probabilityArray = trainstream.probabilityArray
teststream = deploy(teststream,10,'kddNoAttack')
