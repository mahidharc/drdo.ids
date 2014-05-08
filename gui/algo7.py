from algo8 import *
from algo3 import *
from random import *
from numpy import *
from parser import *

def determineThresholdProbability(stream, groupCount, flagArray):
  """
      This module computes the threshold probability which will be used to classify if a particular window is
      either an attack window or not
  """
  #Intialise the probablities of the groups to 0
  parray = zeros(groupCount)
  #Set seed of random number generator
  seed(2)
  #Grouping the learning traffic
  for n in range(groupCount):
    initialValue = randint(0,len(flagArray))
    proportionArray = array([])
    groupRange = round(len(flagArray)/groupCount)
    #Learn from 9/10 th of traffic
    for i in roll(flagArray,flagArray.size-initialValue)[:groupRange]:
      proportionArray=append(proportionArray,i)
    trainingArray = fromstring(flagArray.tostring().replace(proportionArray.tostring(), ""), dtype=flagArray.dtype)
    streamTemp = train(stream, stream.windowSize, stream.bandCount, trainingArray)
    windowCount = len(proportionArray)/stream.windowSize
    window = zeros(stream.windowSize)
    for i in range(windowCount):
      rangeBegin = i*stream.windowSize
      for j in range(rangeBegin,rangeBegin+stream.windowSize):
        window[j%stream.windowSize] = proportionArray[j]
      # Compute probability of remaining 1/10 th of traffic
      probability = determineProbability(window,streamTemp)
      parray=append(parray,probability)
  parraySorted = sort(parray)
  #Sieving lower probabilities
  result = parraySorted[int(len(parray)*(stream.thresholdProbability))+1]
  return result
