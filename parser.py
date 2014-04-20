from numpy import *

def parse(filename):
  flag = [line.strip() for line in open(filename)]
  flags = []
  for i in range(len(flag)):
    flags.append(int(flag[i],0))
  
  flagArray = array([])
  type1 = 4
  
  for i in flags:
    if i&type1 == True:
      flagArray = append(flagArray,1)
    elif i == 2:
      flagArray = append(flagArray,2)
    elif i == 16:
      flagArray = append(flagArray,3)
    elif i == 17:
      flagArray = append(flagArray,4)
    elif i == 24:
      flagArray = append(flagArray,5)
    else:
      flagArray = append(flagArray,6)
  return flagArray