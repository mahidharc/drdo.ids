from numpy import *
from random import *
class TCPstream:
  """
     This class holds information about a praticular stream. A stream is all traffic that can be uniqely
     identified by the combination of application port number and the destination IP
  """
  #Intialise all the attributes to their default values
  destinationIP = ""
  destinationPort = ""
  windowSize = 0
  bandCount = 0
  errorProportion = 0.0
  trainWindowCount = 0
  packetCounter = zeros(6)
  probabilityArray = array([])
  thresholdProbability = 0.0
  attackWindowCount = 0
  normalWindowCount = 0
  stateArr = []
  winNoArr =[]

  def __init__(self,winSize,bandC,t):
    # Constructor to initialize the object
    self.windowSize = winSize
    self.probabilityArray = zeros(self.windowSize*6).reshape(6,self.windowSize)
    self.bandCount = bandC
    self.thresholdProbability = t


def determineProbability(window, stream):
  """
    Probability computation involves computing statistics of a window and determining
    the probability with which the window would have occurred in the training phase
  """
  #Initialize the probability to 1
  probability = 1
  #Initialise the number of packet of each group to 0
  pcount = zeros(6)
  #Update the count of packets falling under each group
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
    if pcount[i] > 99.0:
        pcount[i]=99.0
    #If probability of a particular group and count is 0 then skip the current iteration as it will make
    #the overall probability 0, else find the product
    if stream.probabilityArray[i][pcount[i]] == 0:
      continue
    probability *= stream.probabilityArray[i][pcount[i]]
  return probability