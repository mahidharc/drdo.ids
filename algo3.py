from algo6 import *

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
  flagArray = fromfile("op_flag", dtype = int16, sep = '\n')
  print flagArray
  print trafficStatistics, windowSize, bandCount

  '''for i in range(6):
    band=determineOptimalBands(stream.probabilityArray[i],windowSize,bandCount)
    stream=updateProbabilities(stream,bandCount,bandCount,i)'''


stream = TCPstream(100,40)
train(stream,stream.packetCounter,stream.windowSize,stream.bandCount)