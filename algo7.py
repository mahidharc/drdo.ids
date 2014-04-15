from algo8 import *
from algo3 import *
from random import *
from numpy import *

def determineThresholdProbability(stream, groupCount, flagArray):
  parray = zeros(groupCount)
  for n in range(groupCount):
    initialValue = randint(0,len(flagArray))
    proportionArray = array([])
    groupRange = round(len(flagArray)/groupCount)
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
      probability = determineProbability(window,streamTemp)
      parray=append(parray,probability)
  parraySorted = sort(parray)
  result = parraySorted[int(len(parray)*(stream.thresholdProbability/100))+1]
  return result

stream = TCPstream(100,40)
flagArray=fromfile("op_flag",dtype=int16,sep="\n")
result=determineThresholdProbability(stream,10,flagArray)
print result
