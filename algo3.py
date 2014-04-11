from algo6 import *
from math import *

class TCPstream:
  destinationIP = ""
  destinationPort = ""
  windowSize = 0
  bandCount = 0
  errorProportion = 0.0
  trainWindowCount = 0
  packetCounter = zeros(6)
  probabilityArray = array([])
  thresholdProbability = 0.0

  def __init__(self,winSize,bandC):
    self.windowSize = winSize
    self.probabilityArray = zeros(self.windowSize*6).reshape(6,self.windowSize)
    self.bandCount = bandC


def train(stream,trafficStatistics,windowSize,bandCount):
  flagArray = fromfile("op", dtype = int16, sep = '\n')
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
      savetxt("event", stream.probabilityArray)

    stream.trainWindowCount += 1
    stream.packetCounter = zeros(6)
    print stream.trainWindowCount
  for i in range(0,6):
    band=determineOptimalBands(stream.probabilityArray[i],windowSize-1,bandCount)
    stream=updateProbabilities(stream,bandCount,band,i)
    savetxt("band" + str(i), band)


stream = TCPstream(10,5)
train(stream,stream.packetCounter,stream.windowSize,stream.bandCount)
#To find out the sum of the array : expected Probability=1
arsum=0
for row in range(len(stream.probabilityArray)):
  for col in range(stream.windowSize):
    arsum=arsum+(stream.probabilityArray[row][col])

print arsum
savetxt("capture", stream.probabilityArray)