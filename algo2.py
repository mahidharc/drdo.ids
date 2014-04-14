from algo3 import *
from algo7 import *
from numpy import *

def trainPhase(stream, packetCounter, windowSize, bandCount, errorProportion, groupCount):
  #update model probabilities
  flagArray = fromfile("op_flag", dtype = int16, sep = '\n')
  stream = train(stream, windowSize, bandCount, flagArray)
  #Determine threshold probability for the stream
  stream.thresholdProbability = determineThresholdProbability(stream, groups, flagArray)
  return stream