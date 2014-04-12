from algo3 import *

def trainPhase(stream, packetCounter, windowSize, bandCount, errorProportion):
  #update model probabilities
  stream = train(stream, packetCounter, windowSize, bandCount)
  #Determine threshold probability for the stream
  stream.thresholdProbability = determineThresholdProbability(stream.windowSize,stream.packetCounter,stream.errorProportion)
  return stream