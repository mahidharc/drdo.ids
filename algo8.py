from numpy import *
from random import *
class TCPstream:
  destinationIP = ""
  destinationPort = ""
  windowSize = 0
  bandCount = 0
  errorProportion = 0.0
  trainWindowCount = 0
  packetCounter = zeros(6)
  probabilityArray = array([])
  thresholdProbability = 0.8

  def __init__(self,winSize,bandC):
    self.windowSize = winSize
    self.probabilityArray = zeros(self.windowSize*6).reshape(6,self.windowSize)
    self.bandCount = bandC


def determineProbability(window, stream, flagArray):
  probability = 1
  for i in range(len(window)):
      if flagArray[i] == 1:
        stream.packetCounter[0] += 1
      elif flagArray[i] == 2:
        stream.packetCounter[1] += 1
      elif flagArray[i] == 3:
        stream.packetCounter[2] += 1
      elif flagArray[i] == 4:
        stream.packetCounter[3] += 1
      elif flagArray[i] == 5:
        stream.packetCounter[4] += 1
      else:
        stream.packetCounter[5] += 1
    #TODO the if-elif-else flags statements from algorithm 3
  for i in range(0,6):
    #print i,stream.packetCounter[i]
    probability *= stream.probabilityArray[i][stream.packetCounter[i]]
  for i in range(6):
    stream.packetCounter[i]=0
  return probability