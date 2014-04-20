from algo3 import *
from algo7 import *
from numpy import *

def trainPhase(windowSize, bandCount, groupCount, filename):
  stream = TCPstream(windowSize,bandCount)
  flagArray = parse(filename)
  stream = train(stream, windowSize, bandCount, flagArray)
  #Determine threshold probability for the stream
  stream.thresholdProbability = determineThresholdProbability(stream, groupCount, flagArray)
  return stream

trainstream = TCPstream(100,40)
trainstream = trainPhase(100,40,10,'op_flag')
f = open('thresholdP','w')
f.write(str(trainstream.thresholdProbability))
f.close()