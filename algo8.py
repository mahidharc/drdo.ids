def determineProbability(windowCount, stream):
  p=1
  #determine counts
  for i in range(0,6):
    p=p*stream.probabilityArray[i][stream.packetCounter[i]]

  return p