from algo2 import *
from algo1 import *

t = 0.091
trainstream = TCPstream(100,40,t)
trainstream = trainPhase(100,40,10,"darpatrain",t)
f = open('thresholdP','w')
f.write(str(trainstream.thresholdProbability))
f.close()
teststream = TCPstream(100,40,t)
teststream.probabilityArray = trainstream.probabilityArray
teststream = deploy(teststream,10,'darpaattack1')
print "Number of Attack Windows: "+str(teststream.attackWindowCount)
print "Number of Normal Windows: "+str(teststream.normalWindowCount)
