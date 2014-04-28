from numpy import *
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

def parse(filename):
  flag = [line.strip() for line in open(filename)]
  flags = []
  packetCount =zeros(6)
  for i in range(len(flag)):
    flags.append(int(flag[i],0))
  
  flagArray = array([])
  type1 = 4
  
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
  groups = ("T1" , "T2" , "T3" , "T4" , "T5" , "T6" )
  y_pos = arange(len(groups))
  for i in range(6):
    if packetCount[i] == 0:
      packetCount[i] =1
  plt.barh(y_pos, packetCount, align='center', alpha=0.0)
  plt.yticks(y_pos,groups)
  plt.xlabel("Count")
  plt.ylabel("Groups")
  plt.title("Number of packets in various groups")
  plt.savefig("static/images/groupcount.png")
  return flagArray