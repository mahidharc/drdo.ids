#TODO import stuff

def determineProbability(window, stream):
  probability = 1
  for i in range(len(window)):
    #TODO the if-elif-else flags statements from algorithm 3
  for i in range(0,6):
    probability *= stream.probabilityArray[i][stream.packetCounter[i]]

  return probability