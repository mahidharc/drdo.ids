from algo3 import *
from algo7 import *
from numpy import *

def trainPhase(windowSize, bandCount, groupCount, filename, thresholdP):
  """
     This module initiates training. It calls the training module
     that trains the NBC against the training dataset. It also calls the module
     that determines the threshold probability
  """
   #Create the stream object
  stream = TCPstream(windowSize,bandCount,thresholdP)
  #Read and parser the dataset
  flagArray = parse(filename)
  #Train using the training dataset
  stream = train(stream, windowSize, bandCount, flagArray)
  #Determine threshold probability for the stream
  stream.thresholdProbability = determineThresholdProbability(stream, groupCount, flagArray)
  return stream
