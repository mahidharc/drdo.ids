from algo8 import *
from algo3 import *
from random import *
from numpy import *

def determineThresholdProbability(stream, groupCount, flagArray):
  parray = zeros(groupCount)
  for n in groupCount:
    initialValue = randint(0,len(flagArray))
    proportionArray = array([])
    groupRange = round(len(flagArray)/groupCount)
    #TODO the groups modulus thing
    for i in range(initialValue, initialValue+groupRange):
      append(proportionArray, flagArray[i])
    trainingArray = fromstring(flagArray.tostring().replace(proportionArray.tostring(), ""), dtype=flagArray.dtype)

    streamTemp = train(stream, stream.windowSize, stream.bandCount, trainingArray)
    windowCount = len(proportionArray)/stream.windowSize
    window = zeros(stream.windowSize)
    for i in range(windowCount):
      rangeBegin = i*stream.windowSize
      for j in range(rangeBegin,rangeBegin+stream.windowSize):
        window[j] = proportionArray[j]
      probability = determineProbability(window,streamTemp)
      append(parray,probability)
  parraySorted = sort(parray)
  result = parraySorted[((stream.thresholdProbability/100)*len(parray))+1]
  return result