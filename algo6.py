from numpy import *
from algo5 import *

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

def updateProbabilities(stream, bandCount, band, observableTypeIndex):
    avgCount = 0
    stream.trainWindowCount += bandCount
    for j in range(0,bandCount):
      nelband = band[j][0]
      for k in range(1,nelband+1):
        avgCount += stream.probabilityArray[observableTypeIndex][band[j][k]]
      avgCount += 1
      avgCount /= nelband
      for k in range(1,nelband+1):
        stream.probabilityArray[observableTypeIndex][band[j][k]] = avgCount
      for k in range(1,nelband+1):
        stream.probabilityArray[observableTypeIndex][band[j][k]] /= stream.trainWindowCount
      avgCount = 0
    return stream

stream = TCPstream(10,5);
A = array([500, 291, 271, 36, 222, 111, 1211, 3, 1, 31, 2])
band = determineOptimalBands(A,10,5)
for i in range(1,6):
  stream = updateProbabilities(stream, stream.bandCount, band, i)