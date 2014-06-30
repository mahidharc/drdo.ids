from numpy import *
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

def parse(filename):
  """
     This module read from the input file. It also groups packets into the 6 groups and plots the packet count graph
  """
  #Open the file and read the data
  flag = [line.strip() for line in open(filename)]
  #Intialise the counters
  flags = []
  packetCount =zeros(6)
  for i in range(len(flag)):
    flags.append(int(flag[i],0))

  flagArray = array([])
  type1 = 4
  #Classigy the packets into groups
  for i in flags:
    if i&type1 == True:
      flagArray = append(flagArray,1)
      packetCount[0] += 1
    elif i == 2:
      flagArray = append(flagArray,2)
      packetCount[1] += 1
    elif i == 16:
      flagArray = append(flagArray,3)
      packetCount[2] += 1
    elif i == 17:
      flagArray = append(flagArray,4)
      packetCount[3] += 1
    elif i == 24:
      flagArray = append(flagArray,5)
      packetCount[4] += 1
    else:
      flagArray = append(flagArray,6)
      packetCount[5] += 1
  return flagArray
