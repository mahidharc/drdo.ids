from algo3 import *
from algo7 import *
from numpy import *

def trainPhase(windowSize, bandCount, groupCount):
  stream = TCPstream(windowSize,bandCount)
  flagArray = parse()
  stream = train(stream, windowSize, bandCount, flagArray)
  #Determine threshold probability for the stream
  stream.thresholdProbability = determineThresholdProbability(stream, groupCount, flagArray)
  return stream

mainstream = TCPstream(100,40)
mainstream=trainPhase(100,40,10)
print mainstream.thresholdProbability