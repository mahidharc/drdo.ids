from algo2 import *
from algo1 import *


trainstream = TCPstream(100,40)
trainstream = trainPhase(100,40,10,'train')
f = open('thresholdP','w')
f.write(str(trainstream.thresholdProbability))
f.close()

teststream = TCPstream(100,40)
teststream.probabilityArray = trainstream.probabilityArray
deploy(teststream,10,'attack')