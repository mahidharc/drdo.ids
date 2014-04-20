from algo6 import *
from math import *


def train(stream,windowSize,bandCount,flagArray):
  if flagArray.size % 100 != 0:
    remainder = flagArray.size % 100
    flagArray = flagArray[:flagArray.size-remainder]
  windowCount = ceil(flagArray.size/windowSize)
  windowCount = int(windowCount)
  flagArray = flagArray.reshape(windowCount,windowSize)
  packetCounter = zeros(6)
  for i in range(windowCount):
    for j in range(windowSize):
      if flagArray[i][j] == 1:
        stream.packetCounter[0] += 1
        packetCounter[0] += 1
      elif flagArray[i][j] == 2:
        stream.packetCounter[1] += 1
        packetCounter[1] += 1
      elif flagArray[i][j] == 3:
        stream.packetCounter[2] += 1
        packetCounter[2] += 1
      elif flagArray[i][j] == 4:
        stream.packetCounter[3] += 1
        packetCounter[3] += 1
      elif flagArray[i][j] == 5:
        stream.packetCounter[4] += 1
        packetCounter[4] += 1
      else:
        stream.packetCounter[5] += 1
        packetCounter[5] += 1
    for j in range(0,6):
      if packetCounter[j] == 0:
        continue
      stream.probabilityArray[j][packetCounter[j]] += 1
      packetCounter[j] = 0
    stream.trainWindowCount += 1
  for i in range(0,6):
    band=determineOptimalBands(stream.probabilityArray[i],windowSize-1,bandCount)
    stream=updateProbabilities(stream,bandCount,band,i)
  return stream