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

def TCPtrain(stream,trafficFlow,sizeW,bandC):
    fp=fromfile("op_flag", dtype=int32, sep='\n' )
    for i in range(6):
        band=determineOptimalBands(stream.probabilityArray[i],sizeW,bandC)
        stream=updateProbabilities(stream,bandC,bandC,i)
    return stream