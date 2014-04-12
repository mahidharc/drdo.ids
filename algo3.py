from algo6 import *
from math import *
from algo2 import *


def train(stream,trafficStatistics,windowSize,bandCount):
  flagArray = fromfile("op_flag", dtype = int16, sep = '\n')
  windowCount = ceil(flagArray.size/windowSize)
  windowCount = int(windowCount)
  flagArray = flagArray.reshape(windowCount,windowSize)

#TODO figure out how to write a proper switch statement for the 6 types of flags
  for i in range(windowCount):
    for j in range(windowSize):
      if flagArray[i][j] == 2:
        stream.packetCounter[1] += 1
      elif flagArray[i][j] == 3:
        stream.packetCounter[2] += 1
      elif flagArray[i][j] == 4:
        stream.packetCounter[3] += 1
      elif flagArray[i][j] == 5:
        stream.packetCounter[4] += 1
    for j in range(0,6):
      if stream.packetCounter[j] == 0:
        continue
      stream.probabilityArray[j][stream.packetCounter[j]] += 1
    stream.trainWindowCount += 1
    stream.packetCounter = zeros(6)
  for i in range(0,6):
    band=determineOptimalBands(stream.probabilityArray[i],windowSize-1,bandCount)
    stream=updateProbabilities(stream,bandCount,band,i)



stream = TCPstream(100,40)
train(stream,stream.packetCounter,stream.windowSize,stream.bandCount)