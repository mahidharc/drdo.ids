from algo6 import *
from math import *


def train(stream,windowSize,bandCount,flagArray):
  """
     This module trains the NBC.
  """
  if flagArray.size % 100 != 0:
    remainder = flagArray.size % 100
    flagArray = flagArray[:flagArray.size-remainder]
  #Determine number of windows
  windowCount = ceil(flagArray.size/windowSize)
  windowCount = int(windowCount)
  #Change flagArray from a 1D array to a 2D array with dimensions windowCount, windowSize
  flagArray = flagArray.reshape(windowCount,windowSize)
  #Intialize the count of each group
  packetCounter = zeros(6)
  #Determine the count of each group
  for i in range(windowCount):
    #Iterate over all the windows
    for j in range(windowSize):
      #Iterate over each packet in the window
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
    #Determine and update the event array
    for j in range(0,6):
      if packetCounter[j] == 0:
        continue
      if packetCounter[j] > 99.0:
          packetCounter[j] = 99.0
      stream.probabilityArray[j][packetCounter[j]] += 1
      packetCounter[j] = 0
    #Update number of windows already trained
    stream.trainWindowCount += 1
  for i in range(0,6):
    #For each group determine optimal bands and update the probabilities
    band=determineOptimalBands(stream.probabilityArray[i],windowSize-1,bandCount)
    stream=updateProbabilities(stream,bandCount,band,i)
  return stream