from algo3 import *
from algo7 import *
from numpy import *

def trainPhase(windowSize, bandCount, groupCount, filename, thresholdP):
  stream = TCPstream(windowSize,bandCount,thresholdP)
  flagArray = parse(filename)
  stream = train(stream, windowSize, bandCount, flagArray)
  #Determine threshold probability for the stream
  stream.thresholdProbability = determineThresholdProbability(stream, groupCount, flagArray)
  return stream
