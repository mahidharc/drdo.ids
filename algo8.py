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


def determineProbability(window, stream):
  probability = 1
  for i in range(len(window)):
    #TODO the if-elif-else flags statements from algorithm 3
  for i in range(0,6):
    probability *= stream.probabilityArray[i][stream.packetCounter[i]]

  return probability