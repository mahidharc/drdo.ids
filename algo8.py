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


def determineProbability(window, stream):
  probability = 1
  pcount = zeros(6)
  for i in range(len(window)):
      if window[i] == 1:
        stream.packetCounter[0] += 1
        pcount[0]+=1
      elif window[i] == 2:
        stream.packetCounter[1] += 1
        pcount[1]+=1
      elif window[i] == 3:
        stream.packetCounter[2] += 1
        pcount[2]+=1
      elif window[i] == 4:
        stream.packetCounter[3] += 1
        pcount[3]+=1
      elif window[i] == 5:
        stream.packetCounter[4] += 1
        pcount[4]+=1
      else:
        stream.packetCounter[5] += 1
        pcount[5]+=1
  for i in range(0,6):
    if stream.probabilityArray[i][pcount[i]-1] == 0:
      continue
    probability *= stream.probabilityArray[i][pcount[i]-1]
  return probability