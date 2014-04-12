from numpy import *

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

def trainPhase(stream, packetCounter, windowSize, bandCount, errorProportion):
  #update model probabilities
  stream = train(stream, packetCounter, windowSize, bandCount)
  #Determine threshold probability for the stream
  stream.thresholdProbability = determineThresholdProbability(stream.windowSize,stream.packetCounter,stream.errorProportion)
  return stream